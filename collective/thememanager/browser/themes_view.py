from zope import component
from collective.thememanager import provider

class ThemesView(provider.ProviderController):
    """a listing of theme"""

    def themes(self):
        return self.getThemes()
