# -*- coding: utf-8 -*-

"""
To upload to PyPI, PyPI test, or a local server:
python setup.py bdist_wheel upload -r <server_identifier>
"""

import setuptools
import os

setuptools.setup(
    name="nionswift-experimental-tools",
    version="0.3.0",
    author="Nion Software",
    author_email="swift@nion.com",
    description="Useful experimental tools.",
    packages=["nionswift_plugin.nion_experimental_tools"],
    install_requires=[],
    license='GPLv3',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.5",
    ],
    include_package_data=True,
    python_requires='~=3.5',
)