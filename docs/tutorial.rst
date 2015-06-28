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

.. code-block:: python

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

    >>> for acto in borme.get_actos():
    ...         print(acto)
    ...         
    [...]
    <BormeActo(223969) RUILERENA SL. (4)>
    <BormeActo(223970) REMOTONIO SL. (3)>
    <BormeActo(223971) GARPAPACIA SL. (3)>
    <BormeActo(223972) GARIETOCIA SL. (3)>
    <BormeActo(223973) PROAS INGENIERIA SL. (3)>
    <BormeActo(223974) LORECUALAR SL. (4)>
    <BormeActo(223976) DELCAVO SL. (4)>
    <BormeActo(223977) A. RANDO 2004 SL. (1)>
    <BormeActo(223978) DISTRIBUIDORA MALAGUEÑA DE EXPLOSIVOS SL. (1)>
    <BormeActo(223979) HMFALGARROBO SL. (2)>
    <BormeActo(223980) SERVICIOS BASICOS MALAGA SL. (2)>
    <BormeActo(223981) PALUSTRIS INVERSIONES SL. (1)>
    <BormeActo(223982) LANDEVANT SL. (1)>
    <BormeActo(223983) RESTAURACIONES FERROVIARIAS SL. (1)>
    <BormeActo(223984) BCM GESTION DE SERVICIOS SL. (1)>
    <BormeActo(223986) VIAJES EUROPA TOURS SA. (2)>
    <BormeActo(223987) FUERTE EL ROMPIDO SL. (1)>
    <BormeActo(223988) JEWELLERY THEATRE IBERIA SL. (3)>
    <BormeActo(223989) AF ASESORIA DE EMPRESAS SL. (1)>
    [...]
    >>> acto = borme.get_acto(223978)
    >>> acto
    <BormeActo(223978) DISTRIBUIDORA MALAGUEÑA DE EXPLOSIVOS SL. (1)>
    >>> acto.get_actos()
    {'Datos registrales': 'T 1728, L 641, F 141, S 8, H MA 22254, I/A 10 (21.05.15).', 'Nombramientos': [('Apoderado', {'GRACIAN ALCAIDE ALBERTO JAVIER'})]}

