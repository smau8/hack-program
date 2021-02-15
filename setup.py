#!/usr/bin/env python

"""
Install timezone package. 
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="timezone",
    version="0.0.1",
    description="A package for displaying US timezones",
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=[
    	"pandas",
    	"datetime",
    	"pytz",
    ],
    entry_points={
        "console_scripts": ["timezone = timezone.__main__:run_program"],
    },
)
