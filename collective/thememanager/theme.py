from zope import interface
from zope import schema
from plone.directives import form

from collective.thememanager import interfaces
from collective.thememanager import i18n

class ProxyTheme(object):
    interface.implements(interfaces.ITheme)
    def __init__(self, provider):
        self.provider = provider

class ThemeSchema(form.Schema):
    """Theme schema"""
    name = schema.TextLine(title=i18n.themeschema_name_title)
    description = schema.Text(title=i18n.themeschema_description_title)
    picture = schema.URI(title=i18n.themeschema_picture_title)
    url = schema.URI(title=i18n.themeschema_url_title)
    zipurl = schema.URI(title=i18n.themeschema_zipurl_title)
    author = schema.TextLine(title=i18n.themeschema_author_title)
    version = schema.Int(title=i18n.themeschema_version_title)
