# coding=utf-8

import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='python-operative',
    version='0.1.1',
    author='Jane Kelly & Jeff Revesz',
    author_email='jane.kelly@buzzfeed.com',
    packages=find_packages(),
    test_suite='test',
    install_requires=[
        'nose<2.0.0',
        'pyftpdlib<2.0.0',
        'caliendo<3.0.0',
        'autopep8'
    ],
    include_package_data=True
)
