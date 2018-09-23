#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from glob import glob
from setuptools import setup, find_packages

version = '0.3.3'


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



try:
    os.symlink('../examples', 'bormeparser/examples')
except FileExistsError:
    pass

setup(
    name='bormeparser',
    packages=find_packages(exclude=['*.tests']),
    package_data={
        "bormeparser": glob("examples/*")
    },
    version=version,
    description="bormeparser is a Python library for parsing BORME files",
    long_description=open('README.md', encoding='utf-8').read(),
    author='Pablo Castellano',
    author_email='pablo@anche.no',
    url='https://github.com/PabloCastellano/bormeparser/',
    download_url='https://github.com/PabloCastellano/bormeparser/archive/master.zip',
    keywords=['BORME', 'transparency', 'opendata', 'Spain', 'Registro mercantil', 'Boletín Oficial del Registro Mercantil'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    license="GPLv3+",
    data_files=[('', ['LICENSE.txt'])],
    include_package_data=True,
    zip_safe=False,
    install_requires=get_install_requires(),
    test_suite="bormeparser.tests"
)

os.unlink('bormeparser/examples')
