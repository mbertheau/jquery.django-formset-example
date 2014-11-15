#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import project


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()

packages = [
    'project',
]

package_data = {
}

requires = [
    "Django>=1.7"
]

classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
]

setup(
    name='project',
    version=project.__version__,
    description='Examples for jquery.django-formset',
    long_description=readme,
    packages=packages,
    package_data=package_data,
    install_requires=requires,
    author=project.__author__,
    author_email='mbertheau@gmail.com',
    url='https://github.com/mbertheau/jquery.django-formset',
    license='MIT',
    classifiers=classifiers,
)
