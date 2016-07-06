#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'pygments-mythesis',
    packages = ['mythesis'],
    entry_points = '''[pygments.styles]
                      mythesis = mythesis:MyThesis
                      mythesisbw = mythesis:MyThesisBW''',
)
