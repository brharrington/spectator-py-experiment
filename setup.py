#!/usr/bin/env python

from distutils.core import setup

setup(
    name='netflix-spectator-py',
    version='0.1',
    description='Python library for reporting metrics to Atlas.',
    author='Brian Harrington',
    author_email='netflix-atlas@googlegroups.com',
    license='Apache 2.0',
    url='https://github.com/brharrington/spectator-py/',
    packages=['netflix', 'netflix.spectator'],
)
