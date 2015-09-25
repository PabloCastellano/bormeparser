#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

sys.path.insert(0, 'bormeparser')
from version import __version__, __license__
sys.path.remove('bormeparser')


def get_install_requires():
    """
    parse requirements.txt, ignore links, exclude comments
    """
    requirements = []
    for requirements_file in ('requirements/base.txt',):
        for line in open(requirements_file).readlines():
            line = line.rstrip()
            # skip to next iteration if comment or empty line
            if any([line.startswith('#'), line == '', line.startswith('http'), line.startswith('git'), line == '-r base.txt']):
                continue
            # add line to requirements
            requirements.append(line)
    return requirements


if sys.version_info[0] == 3:
    long_description = open('README.md', encoding='utf-8').read()
else:
    long_description = open('README.md').read()

if sys.argv[-1] == 'publish':
    import os
    os.system("python setup.py sdist bdist_wheel upload -s")
    args = {'version': __version__}
    print("You probably want to also tag the version now:")
    print("  git tag -s -a v%(version)s -m 'version %(version)s'" % args)
    print("  git push --tags")
    sys.exit()

setup(
    name='bormeparser',
    packages=find_packages(exclude=['*.tests']),
    version=__version__,
    description="bormeparser is a Python library for parsing BORME files",
    long_description=long_description,
    author='Pablo Castellano',
    author_email='pablo@anche.no',
    url='https://github.com/PabloCastellano/bormeparser/',
    download_url='https://github.com/PabloCastellano/bormeparser/archive/master.zip',
    keywords=['BORME', 'transparency', 'opendata', 'Spain', 'Registro mercantil', 'Boletín Oficial del Registro Mercantil'],
    license=__license__,
    data_files=[('', ['LICENSE.txt'])],
    include_package_data=True,
    zip_safe=False,
    install_requires=get_install_requires(),
    test_suite="bormeparser.tests"
)
