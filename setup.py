#!/usr/bin/env python
# coding: utf-8
# Copyright 2013-2014 Nick Bargnesi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import lazarus
from setuptools import setup, Command


class _Command(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class PEP8(_Command):
    description = 'PEP8 analysis'

    def run(self):
        code = os.system('scripts/pep8.sh')
        if code != 0:
            sys.exit(1)


class Pyflakes(_Command):
    description = 'Pyflakes analysis'

    def run(self):
        code = os.system('scripts/pyflakes.sh')
        if code != 0:
            sys.exit(1)


class Test(_Command):
    description = 'Run tests'

    def run(self):
        os.system('scripts/test.sh')


class Check(_Command):
    description = 'Run all checks'

    def run(self):
        codes = []
        codes.append(os.system('scripts/pep8.sh'))
        codes.append(os.system('scripts/pyflakes.sh'))
        codes.append(os.system('scripts/test.sh'))
        if any([code != 0 for code in codes]):
            sys.stderr.write('One or more checks have failed.\n')
            sys.stderr.flush()
            sys.exit(1)
        else:
            sys.stdout.write('All checks have passed.\n')
            sys.stdout.flush()


name = 'lazarus'
license = 'Apache License (2.0)'
packages = ['lazarus']
description = 'Restart-on-change library'
author = 'Nick Bargnesi'
author_email = 'nick@den-4.com'
url = 'https://github.com/formwork-io/lazarus'
download_url = 'https://github.com/formwork-io/lazarus/releases'
classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: System :: Monitoring',
    'Topic :: Utilities'
]
install_requires = [
    'watchdog >= 0.8.2'
]
long_description = '''\
Lazarus
-------

A library that restarts the process when source code changes.
'''

setup(
    cmdclass={
        'pep8': PEP8,
        'pyflakes': Pyflakes,
        'test': Test,
        'allchecks': Check
    },
    name=name,
    packages=packages,
    version=lazarus.__version__,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    download_url=download_url,
    classifiers=classifiers,
    install_requires=install_requires,
    long_description=long_description
)
