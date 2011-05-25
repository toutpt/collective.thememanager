from StringIO import StringIO
from urllib2 import urlopen

from zope import component

from plone.app.theming.browser import controlpanel as base

from collective.thememanager import interfaces


class ThemingControlpanel(base.ThemingControlpanel):
    
    def update(self):
        form = self.request.form
        if 'form.button.Import' not in form:
            return super(ThemingControlpanel,self).update()

        themeid = form.get('theme', None)
        
        if themeid is None:
            return super(ThemingControlpanel,self).update()

        tm = self.thememanager()
        theme = tm.getThemeById(themeid)
        url = str(theme.zipurl)
        download = urlopen(url)
        code = download.getcode()
    
        if code != 200:
            raise Exception, 'Cant download theme archive'%code

        content = download.read()
        sio = StringIO(content)
        self.request.form['themeArchive'] = sio
        return super(ThemingControlpanel,self).update()

    def thememanager(self):
        return component.queryUtility(interfaces.IThemeManager)
