# -*- coding: utf-8 -*-
"""
Test suite for acceptance tests in the 'eea.api.glossary' package.

This module defines a test suite for running Robot Framework
acceptance tests in the 'eea.api.glossary' package. It uses the
'plone.testing.layered' approach to apply the
'EEA_API_GLOSSARY_ACCEPTANCE_TESTING' layer to each test case.
"""
import unittest
import os
from eea.api.glossary.testing import EEA_API_GLOSSARY_ACCEPTANCE_TESTING  # noqa: E501
from plone.app.testing import ROBOT_TEST_LEVEL
from plone.testing import layered

import robotsuite


def test_suite():
    """
    Create and return a test suite for acceptance tests.

    This function builds a test suite by discovering Robot Framework test files
    ('.robot' files) in the 'robot' directory and adding them to the suite.
    Each test case is then layered with 'EEA_API_GLOSSARY_ACCEPTANCE_TESTING'.

    Returns:
    unittest.TestSuite: The test suite for acceptance tests.
    """
    suite = unittest.TestSuite()
    current_dir = os.path.abspath(os.path.dirname(__file__))
    robot_dir = os.path.join(current_dir, 'robot')
    robot_tests = [
        os.path.join('robot', doc) for doc in os.listdir(robot_dir)
        if doc.endswith('.robot') and doc.startswith('test_')
    ]
    for robot_test in robot_tests:
        robottestsuite = robotsuite.RobotTestSuite(robot_test)
        robottestsuite.level = ROBOT_TEST_LEVEL
        suite.addTests([
            layered(
                robottestsuite,
                layer=EEA_API_GLOSSARY_ACCEPTANCE_TESTING,
            ),
        ])
    return suite
