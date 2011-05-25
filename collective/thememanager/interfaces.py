from zope import interface
from zope import schema
# -*- Additional Imports Here -*-
from plone.app.theming import interfaces as base

class ITheme(interface.Interface):
    """An proxied diazo theme (remote version)"""
    title = schema.TextLine(title=u"Theme id")
    description = schema.Text(title=u"description")
    picture = schema.URI(title=u"URL of a screenshot")
    url = schema.URI(title=u"Presentation page url")
    zipurl = schema.URI(title=u"Download URL")
    authorname = schema.TextLine(title=u"Author Name")
    version = schema.Int(title=u"Version")

class IThemeProvider(interface.Interface):
    """A theme container"""
    url = schema.URI(title=u"Theme provider url")

    def getThemeIds():
        """Return a list of all theme ids provided"""

    def getThemeById(id):
        """Return the theme with id=id. If the theme doesn't exist it create
        a new one but doesn't create resources. You must use theme manager
        for that. If id is None return None"""

    def getThemes():
        """Return a list of ITheme objects"""


class IThemeManager(IThemeProvider):
    """A theme provider aggregator"""

    def getThemesProviders():
        """Return a list of IThemesProvider. The persistent themesProvider
        is the first, it as precedence on all other ones. It is like the
        custom folder in portal_skin."""

    def addProxyThemeProvider(url):
        """Add a theme provider"""

#FRAMEWORK RELATED INTERFACES

class IThemeManagerLayer(interface.Interface):
    """ A layer specific to this product. 
        Is registered using browserlayer.xml
    """

class IThemeSourcesListFormSchema(interface.Interface):
    """A sources list of theme is a url to a remote """
    sources_list = schema.List(title=u"Sources list",
                               required=True,
                               value_type=schema.URI(title=u"theme provider url"))
