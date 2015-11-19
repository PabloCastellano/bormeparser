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
    downloaded = bormeparser.download_pdf(date, path, bormeparser.SECCION.A, bormeparser.PROVINCIA.MALAGA)

.. code-block:: python

    >>> print(donloaded)
    True

Para conocer la url de un PDF, bormeparser internamente descarga el archivo XML del día y ahí encuentra la ruta.
Podemos obtener dicho archivo XML así:

.. code-block:: python

    >>> bormeparser.download_xml(date, '/tmp/20150602.xml')
    True

Parsear un archivo PDF de BORME:

.. code-block:: python

    borme = bormeparser.parse('/tmp/BORME-A-2015-102-29.pdf')

.. code-block:: python

    >>> print(borme)
    <Borme(2015-06-02) seccion:SECCIÓN PRIMERA provincia:MÁLAGA>

Uso avanzado
------------

Descargar y parsear un PDF de BORME:

.. code-block:: python

    borme = bormeparser.download_pdf(date, path, bormeparser.SECCION.A, bormeparser.PROVINCIA.MALAGA, parse=True)

Si no ha habido ningún error (problema de conexión, el BORME de esa fecha no existe, ...) la variable borme
es una instancia de Borme:

.. code-block:: python

    >>> print(borme)
    <Borme(2015-06-02) seccion:SECCIÓN PRIMERA provincia:MÁLAGA>

Borme y BormeActo
-----------------

De la instancia BORME puedes obtener información básica como la fecha, la sección, la provincia...

.. code-block:: python

    >>> borme.cve
    'BORME-A-2015-102-29'
    >>> borme.num
    102
    >>> borme.info
    {}
    >>> borme.date
    datetime.date(2015, 6, 2)
    >>> borme.provincia
    'MÁLAGA'
    >>> borme.seccion
    'SECCIÓN PRIMERA'

Y lo más importante: los anuncios mercantiles.

.. code-block:: python

    >>> for anuncio in borme.get_anuncios()[:10]:
    ...         print(anuncio)
    ...         
    <BormeAnuncio(223966) POLYESTER MALAGA SA (1)>
    <BormeAnuncio(223967) RED MOUNTAIN PARK SL (3)>
    <BormeAnuncio(223968) ISOFT SANIDAD SA (1)>
    <BormeAnuncio(223969) RUILERENA SL (4)>
    <BormeAnuncio(223970) REMOTONIO SL (4)>
    <BormeAnuncio(223971) GARPAPACIA SL (4)>
    <BormeAnuncio(223972) GARIETOCIA SL (4)>
    <BormeAnuncio(223973) PROAS INGENIERIA SL (2)>
    <BormeAnuncio(223974) LORECUALAR SL (4)>
    <BormeAnuncio(223975) CUALERENA SL (4)>

El segundo número entre paréntesis indica el número de actos mercantiles que contiene dicho anuncio.

Para analizar un anuncio mercantil en concreto, podemos obtenerlo de la instancia Borme a través de su id:

.. code-block:: python

    >>> anuncio = borme.get_anuncio(223969)
    >>> anuncio.datos_registrales
    'T 4889, L 3797, F 13, S 8, H MA109474, I/A 2 (21.05.15).'
    >>> import pprint
    >>> anuncio.get_actos()
    <generator object get_actos at 0x7fed96cceb40>
    >>> actos = list(anuncio.get_actos())
    >>> pprint.pprint(actos)
    [('Ceses/Dimisiones',
      {'Adm. Solid.': {'PASCUAL GARCIA LORENA', 'RUIZ GARRIDO JUAN ANTONIO'}}),
     ('Nombramientos', {'Liquidador': {'PASCUAL GARCIA LORENA'}}),
     ('Disolución', 'Voluntaria.'),
     ('Extinción', True)]
