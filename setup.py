#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup

sys.path.insert(0, 'bormeparser')
from version import __version__, __license__
sys.path.remove('bormeparser')

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
    packages=['bormeparser'],
    version=__version__,
    description="bormeparser is a Python library for parsing BORME files",
    long_description=open('README.md').read(),
    author='Pablo Castellano',
    author_email='pablo@anche.no',
    url='https://github.com/PabloCastellano/bormeparser/',
    download_url='https://github.com/PabloCastellano/bormeparser/archive/master.zip',
    keywords = ['BORME', 'transparency', 'opendata', 'Spain', 'Registro mercantil', 'Boletín Oficial del Registro Mercantil'],
    license=__license__,
    data_files=[('', ['LICENSE.txt'])],
    include_package_data=True,
    zip_safe=False,
    install_requires=['requests', 'pdfminer', 'pyPdf', 'lxml'],
    test_suite = "bormeparser.tests.test_bormeparser"
)
