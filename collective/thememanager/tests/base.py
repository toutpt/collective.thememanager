import unittest2 as unittest
from zope import interface
from plone.app import testing
from collective.thememanager import testing as layer

class UnitTestCase(unittest.TestCase):
    pass

class TestCase(unittest.TestCase):

    layer = layer.INTEGRATION

    def setUp(self):
        from zope.annotation.interfaces import IAttributeAnnotatable
        super(TestCase, self).setUp()
        self.portal = self.layer['portal']
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

class FunctionalTestCase(unittest.TestCase):

    layer = layer.FUNCTIONAL

    def setUp(self):
        from zope.annotation.interfaces import IAttributeAnnotatable
        self.portal = self.layer['portal']
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']
