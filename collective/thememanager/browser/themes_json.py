import json
from collective.thememanager import provider

class ThemesJSON(provider.ProviderController):
    
    def __call__(self):
        themes = self.getThemes()
        themes_json = json.dumps(themes)
        return themes_json
