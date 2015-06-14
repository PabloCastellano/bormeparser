bormeparser
===========

**bormeparser** is a Python library for parsing BORME files (Boletín Oficial del Registro Mercantil in Spain).

[![Travis bormeparser](https://travis-ci.org/PabloCastellano/bormeparser.svg?branch=master)](https://travis-ci.org/PabloCastellano/bormeparser)
[![Pypi bormeparser](https://badge.fury.io/py/bormeparser.png)]( https://pypi.python.org/pypi/bormeparser)
[![Downloads bormeparser](https://img.shields.io/pypi/dm/bormeparser.svg)](https://pypi.python.org/pypi/bormeparser)

What is BORME
=============

The **Boletín Oficial del Registro Mercantil** (Spanish for *Official Mercantile Register Bulletin*) is a document published daily by
Registro Mercantil Central (RMC) in Spain which contains newly created societies, societies that have broken up, and some other data
the companies must communicate.

This library takes advantage of the electronic format of BORMEs that are published since 2009 due to
[this Spanish law](http://www.boe.es/buscar/doc.php?id=BOE-A-2008-19826).

BORMEs are published at http://boe.es/diario_borme/.

Unfortunately due to some agreements with Mercantile Register they are not allowed
to publish all data in some useful format like XML and the most interesting information is only available in PDF files.

You can read more about it on:
- Wikipedia: https://es.wikipedia.org/wiki/Boletín_Oficial_del_Registro_Mercantil

Compiling
=========

lxml package has some parts that need to be compiled and you need the following dependencies:

For Python 3:

    sudo apt-get install python-dev libxslt1-dev

For Python 3:

    sudo apt-get install python3-dev libxslt1-dev


Usage
=====

TBD...

Install
=======

You can install it by typing:

    python setup.py install

or you can get it from PYPI by using pip:

    pip install bormeparser

License
=======
The code license is GPLv3+
