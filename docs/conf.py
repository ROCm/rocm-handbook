"""Configuration file for the Sphinx documentation builder."""

import os
import re
from pathlib import Path

external_projects_remote_repository = ""
external_projects_current_project = "rocm-handbook"
# external_projects = ["amd-gpu-programming-guide"]
external_projects_path = "projects.yaml"

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "rocm-handbook.amd.com")
html_context = {}
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True
project = "ROCm handbook"

version = "1.0.0"
release = version
html_title = "ROCm handbook"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2026 Advanced Micro Devices, Inc. All rights reserved."

# Required settings
html_copy_source = True
html_theme = "rocm_docs_theme"
html_theme_options = {
    "announcement": "Additional content can be found on the <a id='rocm-banner' href='https://rocm.docs.amd.com/en/latest/'>ROCm documentation portal</a>.",
    "flavor": "generic",
    "link_main_doc": False,
    "use_download_button": True,
    "header_title": "AMD ROCm™ Handbook",
    "header_link": "https://rocm-handbook.amd.com/",
    "version_list_link": False,
    "nav_secondary_items": {
        "GitHub": "https://github.com/ROCm/rocm-handbook",
        "Community": "https://github.com/ROCm/TheRock/discussions",
        "Blogs": "https://rocm.blogs.amd.com/",
        "ROCm™ Docs": "https://rocm.docs.amd.com",
        "Instinct™ Docs": "https://instinct.docs.amd.com/",
        "Support": "https://github.com/ROCm/TheRock/issues/new/choose",
        "ROCm Developer Hub": "https://www.amd.com/en/developer/resources/rocm-hub.html",
    },
    # Add any additional theme options here
}
extensions = ["rocm_docs"]

html_static_path = ["_static", "images"]

html_css_files = ["index.css"]

# Table of contents
external_toc_path = "./sphinx/_toc.yml"

exclude_patterns = [".venv"]
