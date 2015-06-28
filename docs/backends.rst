Backends
========

Bormeparser soporta diferentes backends a la hora de parsear los archivos PDF.

Usar un backend específico
--------------------------

.. code-block:: python

    import bormeparser

    parser = bormeparser.backend.pypdf2.parser()
    parser.download(...)


Implementar un nuevo backend
----------------------------

base.py