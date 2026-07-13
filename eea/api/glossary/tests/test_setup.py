"""Tests for setup handlers."""

import unittest

from eea.api.glossary.setuphandlers import HiddenProfiles


class TestHiddenProfiles(unittest.TestCase):
    """Test HiddenProfiles."""

    def setUp(self):
        self.hidden = HiddenProfiles()

    def test_get_non_installable_profiles(self):
        """Test that uninstall profile is hidden."""
        profiles = self.hidden.getNonInstallableProfiles()
        self.assertIsInstance(profiles, list)
        self.assertIn("eea.api.glossary:uninstall", profiles)

    def test_get_non_installable_products(self):
        """Test that upgrades package is hidden."""
        products = self.hidden.getNonInstallableProducts()
        self.assertIsInstance(products, list)
        self.assertIn("eea.api.glossary.upgrades", products)

    def test_profiles_are_strings(self):
        """Test that all profile entries are strings."""
        for profile in self.hidden.getNonInstallableProfiles():
            self.assertIsInstance(profile, str)

    def test_products_are_strings(self):
        """Test that all product entries are strings."""
        for product in self.hidden.getNonInstallableProducts():
            self.assertIsInstance(product, str)

    def test_no_installable_profile_leaked(self):
        """Test that the default profile is NOT hidden."""
        profiles = self.hidden.getNonInstallableProfiles()
        self.assertNotIn("eea.api.glossary:default", profiles)


def test_suite():
    """Test suite."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
