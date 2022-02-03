#!/usr/bin/env python

from distutils.core import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(name='plr-parser',
      version='1.0',
      description='Parser terraria plr file',
      author='liriondev',
      license='GNU General Public License v3.0',
      long_description=long_description,
      packages=['plr_parser', 'plr_parser.src'],
      python_requires=">=3.6"
     )
