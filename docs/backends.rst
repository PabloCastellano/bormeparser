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

Para implementar un nuevo backend, es necesario crear un nuevo paquete en el directorio bormeparser/backends/ con la siguiente estructura::

    nuevoparser/
    ├── __init__.py
    ├── parser.py

`__init__.py` deberá estar vacío.

`parser.py` deberá contener una clase que herede de BormeParserBackend e implemente el método `_parse()`:

.. code-block:: python

    from bormeparser.backends.base import BormeParserBackend
    
    class NuevoParser(BormeParserBackend):
        def _parse(self):
            # Do your parsing here
            return DATA

`_parse()` debe retornar un diccionario de la siguiente forma:

.. code-block:: python

    {214028: {'Actos': {'Ceses/Dimisiones': [('Adm. Unico', {'JUAN GARCIA GARCIA'})],
                        'Datos registrales': 'T 5188, L 4095, F 146, S 8, H MA120039, I/A 4 (25.05.15).',
                        'Nombramientos': [('Adm. Unico', {'PEDRO GOMEZ GOMEZ'})]},
              'Empresa': 'EMPRESA RANDOM SL.'},
     214017: {'Actos': {'Datos registrales': 'T 2226, L 1139, F 102, S 8, H MA 33737, I/A 6 (25.05.15).',
                        'Modificaciones estatutarias': '8. Administración y Representacion.-.'},
              'Empresa': 'EMPRESA ALEATORIA SL.'},
     'borme_fecha': 'Martes 2 de junio de 2015',
     'borme_num': 102,
     'borme_provincia': 'MÁLAGA',
     'borme_seccion': 'SECCIÓN PRIMERA'}

Es decir, debe contener los atributos `borme_fecha`, `borme_num`, `borme_provincia`, `borme_seccion` y todos los actos estructurados de la misma manera.
Para más información consulta el código fuente de los parsers ya disponibles.

Por último añada el nuevo parser a `backends/__init__.py`:

.. code-block:: python

    from .parser1.parser import Parser1
    from .pypdf2.parser import PyPDF2Parser
    from .nuevoparser.parser import NuevoParser

    __all__ = ['parser1', 'pypdf2', 'nuevoparser']
