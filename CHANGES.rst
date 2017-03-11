Changelog
=========

Version 0.3.0 [unreleased]
--------------------------

- Cambios en el formato BORME-JSON
- Usar requests en lugar de urllib


Version 0.2.4 [2016-09-21]
--------------------------

- BormeXML: get_url_pdfs, get_cves y get_sizes ahora permiten especificar sección y provincia
- Nueva constante ALL_PROVINCIAS en bormeparser.provincia
- Detección de nuevos tipos de sociedades
- Scripts: limpieza, uso de argparse en los scripts, unificación de parámetros
- Mejoras menores en la documentación
- Nuevos campos "version" y "raw_version" en el formato JSON de BORME

Version 0.2.3 [2016-04-26]
--------------------------

- Mejora en el parser de BORME C

Version 0.2.2 [2016-04-26]
--------------------------

- Mejoras en el parser de BORME C

Version 0.2.1 [2016-04-25]
--------------------------

- Corregidos fallos de compatibilidad con Python 2

Version 0.2 [2016-04-25]
------------------------

- Eliminado primer argumento "date" de BormeXML.get_url_pdfs()
- Nuevo método: BormeXML.get_urls_cve()
- Arregladas algunas incompatibilidades con Python 2
- Nuevas funciones: get_borme_website(), get_url_seccion_c()
- Se incorpora parser para BORME C
- Añadido el acto "(Primera inscripcion O.M. 10/6/1.997)"
- Renombradas constantes y funciones
- BormeXML: BORME C
- script download_borme_pdfs_C.py
- Mejora parsing de cargos repetidos en el mismo acto (issue #4)

Version 0.1.5 [2015-09-25]
--------------------------

- Añadidos nuevos cargos
- Mejoras en setuptools

Version 0.1.4 [2015-09-24]
--------------------------

- Grandes mejoras en el parser en general
- Añadidos cargos y actos nuevos
- Mejoras en las expresiones regulares
- Los objetos Provincia ahora son comparables
- download_pdfs() ahora admite los parámetros seccion y provincia
- Nuevos scripts: borme_to_json, download_borme_pdfs_A, borme_sort, xml_poller
- Uso de OrderedDict en lugar de dict
- Uso de OrderedDict en lugar de dict
- Usar la librería logging
- Más tests
- Actualización de los requisitos

Version 0.1.3 [2015-08-08]
--------------------------

- Fixed missing packages that weren't distributed

Version 0.1.2 [2015-08-07]
--------------------------

- Fixed UnicodeWarning that caused tests to fail in Python 2

Version 0.1.1 [2015-08-07]
--------------------------

- setup.py install now installs requirements

Version 0.1 [2015-08-07]
------------------------

- First release
- Download and parse BORME PDF files
- Main parser is PyPDF2 
- Python 2 and 3 support
- Tests suite
