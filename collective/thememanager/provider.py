import json

from urllib2 import urlopen

from zope import interface

from collective.thememanager import interfaces
from collective.thememanager import theme
from Products.CMFCore.utils import getToolByName

class Provider(object):
    interface.implements(interfaces.IThemeProvider)
    def __init__(self, url):
        self.themes = {}
        self.url = url
        self._initialized = False

    def getThemeIds(self):
        return self.themes.keys()

    def getThemeById(self, id):
        return self.themes.get(id,None)

    def getThemes(self):
        return self.themes.values()

#TODO: memoize
    def _initialize(self):
        if self._initialized:return
        download = urlopen(self.url)
        code = download.getcode()
    
        if code != 200:
            raise Exception, 'Cant download source list'%code
        if download.info().type != 'application/json':
            raise Exception, 'Is not json mimetype'
        content = download.read()
        d = json.loads(content)
        metathemes = d['themes']
        themeids = self.getThemeIds()
        for metatheme in metathemes:
            if metatheme['zipurl'] in themeids:
                continue
            t = theme.Theme(self, **metatheme)
            self.themes[t.zipurl] = t
        self._initialized=True


from Products.Five import BrowserView

class JSONProviderView(BrowserView):
    """A view to create a json input to create a proxy provider"""
    def __call__(self):
        metadatas = self.getThemesMetadatas()
        metadatas_json = json.dumps(metadatas)
        return metadatas_json

    #TODO: memoize
    def getThemesMetadatas(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(portal_type='Theme')
        objs = [brain.getObject() for brain in brains]
        def metadata(ob):
            return {'name':ob.Title(),
                    'description':ob.Description(),
                    'picture':'',
                    'url':ob.absolute_url(),
                    'zipurl':'',
                    'authorname':ob.Creators()[0],
                    'version':ob.ModifiedDate()}
        metadatas = map(metadata, objs)
        return metadatas
