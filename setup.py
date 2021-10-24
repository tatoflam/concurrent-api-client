#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

def get_readme():
    """ Get the README from the current directory. If there isn't one, return an empty string """
    all_readmes = sorted(glob("README*"))
    if len(all_readmes) > 1:
        warnings.warn("There seems to be more than one README in this directory. Choosing the "
                      "first in lexicographic order.")
    if len(all_readmes) > 0:
        return open(all_readmes[0], 'r').read()

    warnings.warn("There doesn't seem to be a README in this directory.")
    return ""

setup(
    name='python_api_client',
    version='1.0',
    license='MIT',
    description='An example for API client using python request library',
    long_description="\n" + get_readme(),
    author='tatoflam',
    author_email='tatoflam@gamil.com',
    url='https://github.com/tatoflam/python_api_client',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    project_urls={
#        'Changelog': 'https://github.com/tatoflam/python_api_client/blob/master/CHANGELOG.rst',
        'Issue Tracker': 'https://github.com/tatoflam/python_api_client/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=3.7',
    install_requires=[
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    setup_requires=[
        'pytest-runner',
    ],
    entry_points={
        # 'console_scripts': [
        #     'nameless = nameless.cli:main',
        # ]
    },
)