#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""    
    Utility to export google authenticator accounts.

    2021-∞ (c) blurryroots innovation qanat OÜ. All rights reserved.
    See license.md for details.

    https://think-biq.com
"""

import setuptools
import setuptools.dist
import os
from src.version import version


PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(PROJECT_PATH, 'readme.md'), 'r') as fh:
    long_description = fh.read()


class BinaryDistribution(setuptools.dist.Distribution):
    """
    Distribution which always forces a binary package with platform name.
    Thanks to https://stackoverflow.com/a/36886459/949561
    """
    def has_ext_modules(foo):
        return True


setuptools.setup(
    python_requires='>=3.9',
    name="gaeh",
    version=version(),
    description="Google Authenticator Export Helper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir = {
        'gaeh': 'src', 
        'gaeh.exporters': 'src/exporters',
        'gaeh.protobuf_migration': 'src/protobuf_migration',
    },
    packages=[
        'gaeh',
        'gaeh.exporters',
        'gaeh.protobuf_migration'
    ],
    include_package_data=True,    
    package_data={'gaeh.protobuf_migration': ['*.proto']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author="biq",
    author_email="sf@think-biq.com",
    url="https://gitlab.com/think-biq/gaeh",
    distclass=BinaryDistribution
)