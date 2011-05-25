from zope import component
from zope import interface

from plone.registry.interfaces import IRegistry

from collective.thememanager import interfaces
from collective.thememanager import provider

class Manager(object):
    interface.implements(interfaces.IThemeManager)
    def __init__(self):
        self._site = None
        self._sourceslist = []
        self._themeids = []
        self._themes = []
    
    def getThemeIds(self):
        if self._themeids:
            return self._themeids
        providers = self.getThemesProviders()
        themeids = []
        for provider in providers:
            themeids.extend(provider.getThemeIds())
        self._themeids = list(set(themeids))
        return self._themeids

    def getThemeById(self,id):
        providers = self.getThemesProviders()
        for provider in providers:
            if id in provider.getThemeIds():
                return provider.getThemeById(id)

    def getThemes(self):
        if self._themes:
            return self._themes
        providers = self.getThemesProviders()
        themes = []
        for provider in providers:
            themes.extend(provider.getThemes())
        self._themes = list(set(themes))
        return self._themes

    def getThemesProviders(self):
        if not self._sourceslist:
            registry = component.getUtility(IRegistry)
            sl = registry.records.get('collective.thememanager.sourceslist',None)
            if sl is not None:
                self._sourceslist = sl.value

        return map(provider.Provider, self._sourceslist)
