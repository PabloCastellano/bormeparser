Backends
========

Bormeparser soporta diferentes backends a la hora de parsear los archivos PDF.

Usar un backend específico
--------------------------

.. code-block:: python

    import bormeparser.backends.pypdf2

    parser = bormeparser.backends.pypdf2.parser.PyPDF2Parser('pdf/BORME-A-2015-27-10.pdf')
    borme = parser.parse()


Implementar un nuevo backend
----------------------------

base.py