# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest
from eea.api.glossary.testing import (
  EEA_API_GLOSSARY_INTEGRATION_TESTING  # noqa: E501
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that eea.api.glossary is properly installed."""

    layer = EEA_API_GLOSSARY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if eea.api.glossary is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'eea.api.glossary'))

    def test_browserlayer(self):
        """Test that IEeaApiGlossaryLayer is registered."""
        from eea.api.glossary.interfaces import IEeaApiGlossaryLayer
        from plone.browserlayer import utils
        self.assertIn(
            IEeaApiGlossaryLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):
    """
    Unit tests for the uninstallation process of the 'eea.api.glossary'
    product.

    This test class is intended to verify the correct behavior of the
    uninstallation process for the 'eea.api.glossary' product. It ensures
    that the product can be successfully uninstalled and that the system is
    left in a consistent state.
    """

    layer = EEA_API_GLOSSARY_INTEGRATION_TESTING

    def setUp(self):
        """
        Set up the test environment for uninstalling the
        'eea.api.glossary' product.

        This method performs the following steps:
        1. Get the Plone portal and installer tool.
        2. Temporarily elevate the test user's role to 'Manager'.
        3. Uninstall the 'eea.api.glossary' product using the Plone
           installer tool.
        4. Restore the test user's original roles.

        This ensures that the product is uninstalled and the system is
        left in a consistent state for further testing.

        Returns:
        None
        """
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('eea.api.glossary')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if eea.api.glossary is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'eea.api.glossary'))

    def test_browserlayer_removed(self):
        """Test that IEeaApiGlossaryLayer is removed."""
        from eea.api.glossary.interfaces import IEeaApiGlossaryLayer
        from plone.browserlayer import utils
        self.assertNotIn(IEeaApiGlossaryLayer, utils.registered_layers())
