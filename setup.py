#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import find_packages, setup

NAME = "eclectic"
DESCRIPTION = "Eclectic Python Web Framework built by Eclecticlly."
EMAIL = "max@eclecticlly.com"
AUTHOR = "Massimiliano Bertinetti"
REQUIRES_PYTHON = ">=3.9.0"
VERSION = "0.0.2"

REQUIRED = [
    "Jinja2==3.0.3",
    "parse==1.19.0",
    "requests==2.27.1",
    "requests-wsgi-adapter==0.4.1",
    "WebOb==1.8.7",
    "whitenoise==6.0.0",
]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=["test_*"]),
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.9",
    ],
    setup_requires=["wheel"],
)
