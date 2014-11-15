#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import skeleton


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()

packages = [
    'skeleton',
]

package_data = {
}

requires = [
]

classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='python-skeleton',
    version=skeleton.__version__,
    description='Skeleton package for Python modules.',
    long_description=readme,
    packages=packages,
    package_data=package_data,
    install_requires=requires,
    author=skeleton.__author__,
    author_email='python@chrisstreeter.com',
    url='https://github.com/streeter/python-skeleton',
    license='MIT',
    classifiers=classifiers,
)
