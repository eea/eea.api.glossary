# -*- coding: utf-8 -*-
"""Installer for the eea.api.glossary package."""

from os.path import join
from setuptools import find_packages
from setuptools import setup

long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open(join("docs", "HISTORY.txt")).read(),
    ]
)

NAME = "eea.api.glossary"
PATH = ["src"] + NAME.split(".") + ["version.txt"]
VERSION = open(join(*PATH)).read().strip()

setup(
    name=NAME,
    version=VERSION,
    description="An API for the volto-eea-slate-glossary addon",
    long_description_content_type="text/x-rst",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="laszlocseh",
    author_email="laszlo.cseh@eaudeweb.ro",
    url="https://github.com/collective/eea.api.glossary",
    project_urls={
        "PyPI": "https://pypi.org/project/eea.api.glossary/",
        "Source": "https://github.com/eea/eea.api.glossary",
        "Tracker": "https://github.com/eea/eea.api.glossary/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["eea", "eea.api"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "z3c.jbot",
        "plone.api>=1.8.4",
        "plone.app.dexterity",
        "elasticsearch==8.17.2",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            "plone.testing>=5.0.0",
            "plone.app.contenttypes",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = eea.api.glossary.locales.update:update_locale
    """,
)
