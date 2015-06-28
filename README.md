< [English version here](README_en.md) >

bormeparser
===========

**bormeparser** es una librería de Python para parsear los archivos del BORME (Boletín Oficial del Registro Mercantil en España).

[![Travis bormeparser](https://travis-ci.org/PabloCastellano/bormeparser.svg?branch=master)](https://travis-ci.org/PabloCastellano/bormeparser)
[![Pypi bormeparser](https://badge.fury.io/py/bormeparser.png)]( https://pypi.python.org/pypi/bormeparser)
[![Downloads bormeparser](https://img.shields.io/pypi/dm/bormeparser.svg)](https://pypi.python.org/pypi/bormeparser)
[![Coverage Status](https://coveralls.io/repos/PabloCastellano/bormeparser/badge.svg)](https://coveralls.io/r/PabloCastellano/bormeparser)
[![Documentation Status](https://readthedocs.org/projects/bormeparser/badge/?version=latest)](https://readthedocs.org/projects/bormeparser/?badge=latest)

Qué es BORME
============

El **Boletín Oficial del Registro Mercantil** es un documento publicado diariamente por el Registro Mercantil Central (RMC)
en España que contiene un listado de las últimas sociedades creadas y disueltas así como otros datos que las empresas
están obligadas a comunicar.

La librería aprovecha que desde la aprobación de [esta ley](http://www.boe.es/buscar/doc.php?id=BOE-A-2008-19826),
desde el año 2009 el BORME se publica también en formato electrónico con la misma validez que su versión en papel.

Los BORMEs se publican en http://boe.es/diario_borme/.

Desgraciadamente debido al acuerdo actual con el Registro Mercantil, no pueden publicar todos los datos en un formato
útil y reutilizable como XML o JSON y los datos más interesantes están solo disponibles en los archivos PDF.

Puedes leer más sobre ello en:
- Wikipedia: https://es.wikipedia.org/wiki/Boletín_Oficial_del_Registro_Mercantil

Compilar
=========

El paquete lxml tiene una parte que necesita ser compilada y requiere las siguientes dependencias:

Para Python 2:

    sudo apt-get install python-dev libxslt1-dev

Para Python 3:

    sudo apt-get install python3-dev libxslt1-dev


Documentación y uso
===================

El directorio docs/ contiene toda la documentación. Puedes generarla ejecutando:

    cd docs && make html

Puedes consultar la versión online en http://bormeparser.readthedocs.org/es/latest/.


Instalación
===========

Puedes instalar bormeparser descargándolo y ejecutando:

    python setup.py install

o puedes obtenerlo desde PyPI así:

    pip install bormeparser

Tests
=====

Este paquete contiene tests unitarios. Puedes ejecutarlos escribiendo alguna de estas órdenes:

    python setup.py test
    python -m unittest bormeparser.tests.test_bormeregex


Licencia
========

Todo el código está bajo licencia GPLv3+.
