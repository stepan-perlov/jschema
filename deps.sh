#!/usr/bin/env bash

# jschema dependencies
wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
sudo pip install PyYAML
sudo pip install jinja2

# develop dependencies
# invoke - run tasks.py file
# twine - upload to pip
# Sphinx - documentation toolkit for python
# sphinx_rtd_theme - documentation theme
# sphinx-pypi-upload - upload doc to pip
sudo pip install invoke
sudo pip install twine
sudo pip install Sphinx
sudo pip install sphinx_rtd_theme
sudo pip install sphinx-pypi-upload
