import json
from collective.thememanager import provider

class ThemesJSON(provider.ProviderController):
    
    def __call__(self):
        themes = self.getThemes()
        themes_json = json.dumps(themes)
        self.request.response.setHeader("Content-type","application/json")
        return themes_json
