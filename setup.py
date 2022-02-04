#!/usr/bin/env python

from distutils.core import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(name='plr-parser',
      version='1.1',
      description='Parser terraria plr file',
      author='liriondev',
      license='GNU General Public License v3.0',
      long_description=long_description,
      download_url='https://github.com/liriondev/plr-parser/archive/refs/tags/v_1.1.zip',
      packages=['plr_parser', 'plr_parser.src'],
      python_requires=">=3.6"
     )
