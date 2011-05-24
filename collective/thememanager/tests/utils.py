class FakeTheme(object):
    def __init__(self, provider):
        self.name = u""
        self.description = u""
        self.picture = "http://www.toto.com/mytheme/mycapture.jpg"
        self.url     = "http://www.toto.com/mytheme"
        self.zipurl  = "http://www.toto.com/mytheme/mycapture.jpg"
        self.authorname = u"JeanMichel FRANCOIS"
        self.version = 10
        self.provider = provider

class FakeThemeProvider(object):

    def __init__(self, url):
        self.themes = {}
        self.url = url

    def getThemeIds(self):
        return self.themes.keys()

    def getThemeById(self, id):
        return self.themes.get(id,None)

    def getThemes(self):
        return self.themes.values()

class FakeThemeManager(object):

    def __init__(self):
        self.providers = {}

    def getThemesProviders(self):
        return self.providers.values()

    def addProxyThemeProvider(url):
        if url not in self.providers.keys():
            self.providers[url] = FakeThemeProvider(url, self)
