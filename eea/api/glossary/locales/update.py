# -*- coding: utf-8 -*-
"""Update locale folders"""

import os
import subprocess
import pkg_resources


domain = "eea.api.glossary"
os.chdir(pkg_resources.resource_filename(domain, ""))
os.chdir("../../../")
target_path = "src/eea.api/glossary/"
locale_path = target_path + "locales/"
i18ndude = "./bin/i18ndude"

# ignore node_modules files resulting in errors
excludes = '"*.html *json-schema*.xml"'


def locale_folder_setup():
    """
    Set up locale folders and initialize message catalogs for each language.

    This function changes the current working directory to the 'locale_path'
    and creates the necessary folders and files for internationalization and
    localization using the gettext module.

    It iterates through the subdirectories in the current directory, assumes
    each subdirectory represents a language, and checks if the 'LC_MESSAGES'
    folder exists. If not, it creates the 'LC_MESSAGES' folder and initializes
    the message catalog for the specified 'domain' using the 'msginit' command.

    Parameters:
    None

    Returns:
    None

    Note:
    - 'locale_path' should be set before calling this function to the desired
      path containing language folders.
    - 'domain' should be set to the desired domain for message catalogs.
    """
    os.chdir(locale_path)
    languages = [d for d in os.listdir(".") if os.path.isdir(d)]
    for lang in languages:
        folder = os.listdir(lang)
        if "LC_MESSAGES" in folder:
            continue
        else:
            lc_messages_path = lang + "/LC_MESSAGES/"
            os.mkdir(lc_messages_path)
            cmd = (
                "msginit --locale={0} "
                "--input={1}.pot "
                "--output={0}/LC_MESSAGES/{1}.po".format(
                    lang,
                    domain,
                )
            )  # NOQA: E501
            subprocess.call(
                cmd,
                shell=True,
            )

    os.chdir("../../../../")


def _rebuild():
    """
    Rebuild compiled message catalogs for the specified domain.

    This function uses the 'i18ndude' tool to rebuild compiled message
    catalogs for the specified 'domain'. It calls the 'rebuild-pot' command
    to update the '.pot' file and create or update the '.po' files in the
    specified 'target_path'. Exclusions can be specified to exclude certain
    files or directories during the rebuild.

    Parameters:
    None

    Returns:
    None
    """
    cmd = (
        "{i18ndude} rebuild-pot --pot {locale_path}/{domain}.pot "
        "--exclude {excludes} --create {domain} {target_path}".format(
            i18ndude=i18ndude,
            locale_path=locale_path,
            domain=domain,
            target_path=target_path,
            excludes=excludes,
        )
    )  # NOQA: E501
    subprocess.call(
        cmd,
        shell=True,
    )


def _sync():
    """
    Synchronize message templates and existing translations.

    This function uses the 'i18ndude' tool to synchronize message
    templates and existing translations. It calls the 'sync' command
    to update the '.pot' file with new messages and update existing
    '.po' files in the 'LC_MESSAGES' folders within the specified
    'locale_path'.

    Parameters:
    None

    Returns:
    None
    """
    cmd = "{0} sync --pot {1}/{2}.pot {1}*/LC_MESSAGES/{2}.po".format(
        i18ndude,
        locale_path,
        domain,
    )
    subprocess.call(
        cmd,
        shell=True,
    )


def update_locale():
    """
    Perform updates to the localization setup.

    Parameters:
    None

    Returns:
    None
    """
    locale_folder_setup()
    _sync()
    _rebuild()
