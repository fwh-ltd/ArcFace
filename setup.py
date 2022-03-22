import os
from setuptools import setup

setup(
  name = 'ArcFace',
  version = '0.0.8',
  install_requires=['tensorflow','gdown'],
  packages = ['ArcFace'],
  setup_requires=['setuptools_scm'],
  include_package_data=True,
)
