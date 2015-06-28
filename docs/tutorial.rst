Tutorial
========

Uso básico
----------

bormeparser proporciona distintas funciones para tratar los archivos del BORME.

Empezamos con las funciones para generar las urls de descarga:

.. code-block:: python

    import bormeparser
    date = (2015, 6, 2)
    xml_url = bormeparser.get_url_xml(date)
    pdf_url = bormeparser.get_url_pdf(date, bormeparser.SECCION.A, bormeparser.PROVINCIA.MALAGA)

.. code-block:: python

    >>> print(xml_url)
    http://www.boe.es/diario_borme/xml.php?id=BORME-S-20150602
    >>> print(pdf_url)
    http://boe.es/borme/dias/2015/06/02/pdfs/BORME-A-2015-102-29.pdf

Pero podemos usar otras funciones para descargar el BORME directamente de ese día:

.. code-block:: python

    import bormeparser
    
    date = (2015, 6, 2)
    path = '/tmp/BORME-A-2015-102-29.pdf'
    borme = bormeparser.download_pdf(date, path, bormeparser.SECCION.A, bormeparser.PROVINCIA.MALAGA)

Si no ha habido ningún error (problema de conexión, el BORME de esa fecha no existe, ...) la variable borme
es una instancia de Borme:

.. code-block:: python

    >>> print(borme)
    <Borme(2015-06-02) seccion:A provincia:29>

Para conocer la url de un PDF, bormeparser internamente descarga el archivo XML del día y ahí encuentra la ruta.
Podemos obtener dicho archivo XML así:

.. code-block:: python

    >>> bormeparser.download_xml(date, '/tmp/20150602.xml')
    True


Uso avanzado
------------