#!/usr/bin/env python
#
# Copyright 2013 Nicolas Lamirault <nicolas.lamirault@gmail.com>.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#


PROJECT = 'python-freeboxclient'

# Change docs/sphinx/conf.py too!
VERSION = '0.1.0'

from setuptools import setup, find_packages

try:
    long_description = open('README.md', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='A client for the FreeboxOS.',
    long_description=long_description,

    author='Nicolas Lamirault',
    author_email='nicolas.lamirault@gmail.com',

    url='https://github.com/nlamirault/python-freeboxclient',
    download_url='https://github.com/nlamirault/python-freeboxclient/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff', 'requests'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'freeboxos = freeboxclient.freeboxos:main'
        ],
        'freeboxos': [
            'about = freeboxclient.simple:About',
            'config = freeboxclient.simple:Configuration',
            'freebox version = freeboxclient.client:FreeboxApiVersion',
            'freebox login = freeboxclient.client:FreeboxLogin',
        ],
    },

    zip_safe=False,
)
