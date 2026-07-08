"""Test layer for eea.api.glossary."""

from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile

import eea.api.glossary


class EeaApiGlossaryLayer(PloneSandboxLayer):
    """Test layer for eea.api.glossary."""

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=eea.api.glossary)

    def setUpPloneSite(self, portal):
        """Set up Plone site."""
        applyProfile(portal, "eea.api.glossary:default")


EEA_API_GLOSSARY_FIXTURE = EeaApiGlossaryLayer()

EEA_API_GLOSSARY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EEA_API_GLOSSARY_FIXTURE,),
    name="EeaApiGlossaryLayer:IntegrationTesting",
)
