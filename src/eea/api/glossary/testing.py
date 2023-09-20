# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import eea.api.glossary


class EeaApiGlossaryLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=eea.api.glossary)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'eea.api.glossary:default')


EEA_API_GLOSSARY_FIXTURE = EeaApiGlossaryLayer()


EEA_API_GLOSSARY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EEA_API_GLOSSARY_FIXTURE,),
    name='EeaApiGlossaryLayer:IntegrationTesting',
)


EEA_API_GLOSSARY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EEA_API_GLOSSARY_FIXTURE,),
    name='EeaApiGlossaryLayer:FunctionalTesting',
)


EEA_API_GLOSSARY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EEA_API_GLOSSARY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EeaApiGlossaryLayer:AcceptanceTesting',
)
