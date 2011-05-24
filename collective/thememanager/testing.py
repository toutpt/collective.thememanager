from plone.testing import z2

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting

class CollectiveThemeManagerLayer(PloneSandboxLayer):
    default_bases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.thememanager
        import plone.app.registry
        import plone.resource
        import plone.namedfile

        self.loadZCML(package=plone.resource)
        self.loadZCML(package=plone.namedfile)
        self.loadZCML(package=plone.app.registry)
        self.loadZCML(package=collective.thememanager)

        # Install product and call its initialize() function
        z2.installProduct(app, 'collective.thememanager')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'collective.thememanager:default')

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'collective.thememanager')

FIXTURE = CollectiveThemeManagerLayer()

INTEGRATION = IntegrationTesting(bases=(FIXTURE,), name="ThemManager:Integration")
FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,), name="ThemManager:Functional")
