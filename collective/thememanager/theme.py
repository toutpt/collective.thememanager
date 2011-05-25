from zope import interface
from zope import schema
from plone.directives import form
from plone.namedfile import field as filefield
from collective.thememanager import interfaces
from collective.thememanager import i18n

class ProxyTheme(object):
    interface.implements(interfaces.ITheme)
    def __init__(self, provider):
        self.provider = provider

class ThemeSchema(form.Schema):
    """Theme schema"""
    picture = filefield.NamedImage(title=i18n.themeschema_picture_title)
    zip     = filefield.NamedFile(title=i18n.themeschema_zip_title)
    author = schema.TextLine(title=i18n.themeschema_author_title)
    version = schema.Int(title=i18n.themeschema_version_title)
