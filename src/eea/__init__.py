# -*- coding: utf-8 -*-
"""
Declare a namespace using pkg_resources for the current module.

This script utilizes the `pkg_resources` module to declare a
namespace for the current module. Namespaces help organize and
prevent naming conflicts in larger projects.
"""
__import__("pkg_resources").declare_namespace(__name__)
