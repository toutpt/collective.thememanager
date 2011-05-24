from zope import interface
from collective.thememanager import interfaces

class Manager(object):
    interface.implements(interfaces.IThemeManager)
    def __init__(self):
        pass
