< [English version here](README_en.md) >

[![Travis bormeparser](https://travis-ci.org/PabloCastellano/bormeparser.svg?branch=master)](https://travis-ci.org/PabloCastellano/bormeparser)
[![Pypi bormeparser](https://badge.fury.io/py/bormeparser.png)]( https://pypi.python.org/pypi/bormeparser)
[![Downloads bormeparser](https://img.shields.io/pypi/dm/bormeparser.svg)](https://pypi.python.org/pypi/bormeparser)
[![Coverage Status](https://coveralls.io/repos/PabloCastellano/bormeparser/badge.svg)](https://coveralls.io/r/PabloCastellano/bormeparser)
[![Documentation Status](https://readthedocs.org/projects/bormeparser/badge/?version=latest)](https://readthedocs.org/projects/bormeparser/?badge=latest)

**NOTA: Este repositorio se encuentra desmantenido. Si buscas una solución para acceder a la información mercantil mediante API y con soporte para empresas, consulta [LibreBOR](https://librebor.me) y [Documentación LibreBOR API](https://docs.librebor.me/).**

bormeparser
===========

**bormeparser** es una librería de **Python 3** para parsear los archivos del BORME (Boletín Oficial del Registro Mercantil en España).

Qué es BORME
============

El **Boletín Oficial del Registro Mercantil** es un documento publicado diariamente por el Registro Mercantil Central (RMC)
en España que contiene un listado de las últimas sociedades creadas y disueltas así como otros datos que las empresas
están obligadas a comunicar.

La librería aprovecha que desde la aprobación de [esta ley](https://www.boe.es/buscar/doc.php?id=BOE-A-2008-19826),
desde el año 2009 el BORME se publica también en formato electrónico con la misma validez que su versión en papel.

Los BORMEs se publican en https://boe.es/diario_borme/.

Desgraciadamente debido al acuerdo actual con el Registro Mercantil, no pueden publicar todos los datos en un formato
útil y reutilizable como XML o JSON y los datos más interesantes están solo disponibles en los archivos PDF.

Puedes leer más sobre ello en:
- Wikipedia: https://es.wikipedia.org/wiki/Boletín_Oficial_del_Registro_Mercantil


Documentación y uso
===================

El directorio docs/ contiene toda la documentación. Puedes generarla ejecutando:

    cd docs && make html

Si quieres generarla para otro idioma (inglés en este caso):

    make -e SPHINXOPTS="-D language='en'" html

Puedes consultar la versión online en http://bormeparser.readthedocs.org/es/latest/.


Instalación desde Git
=====================

Puedes instalar bormeparser descargándolo y ejecutando:

    sudo apt-get install python3-dev libxslt1-dev libffi-dev zlib1g-dev gcc
    git clone https://github.com/PabloCastellano/bormeparser.git
    cd bormeparser
    python setup.py install


Instalación desde Pip
=====================

    pip install bormeparser


Scripts
=======

La carpeta scripts/ contiene algunos scripts útiles para tratar archivos BORME. Todos tienen parámetros de entrada similares.

    python scripts/download_borme_pdfs.py -f init -p VALENCIA
    python scripts/check_bormes.py -f init -p VALENCIA
    python scripts/download_borme_pdfs.py -d /tmp/bormemadrid -p MADRID -f 2016-06-01 -t 2016-06-30
    python scripts/check_bormes.py -d /tmp/bormemadrid -p MADRID -f 2016-06-01 -t 2016-06-30
    python scripts/borme_json_all.py -d /tmp/bormemadrid

Tests
=====

Este paquete contiene tests unitarios. Puedes ejecutarlos escribiendo alguna de estas órdenes:

    python setup.py test
    python -m unittest bormeparser.tests.test_borme
    python -m unittest bormeparser.tests.test_bormeparser
    python -m unittest bormeparser.tests.test_bormeregex


Licencia
========

Todo el código está bajo licencia GPLv3+. Para más información consulta el archivo LICENSE.txt
