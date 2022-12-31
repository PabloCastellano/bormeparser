Changelog for bormeparser
=========================

0.5.2 (unreleased)
------------------

- New force download flag in download_url()


0.5.1 (unreleased)
------------------

- Nothing changed yet.


0.5.0 (2022-09-27)
------------------

- Actualizadas las dependencias
- Bormeparser requiere Python 3.6+ ahora
- Añadido Dockerfile


0.4.2 (2021-03-01)
------------------

- Actualizadas las dependencias


0.4.1 (2021-02-15)
------------------

- No generar universal wheel (py2 ya no está soportado)
- Detectar cargo "AUDIT.INDIV."
- Pequeñas mejoras en scripts check_bormes.py y download_borme_pdf.py
- Actualizada dependencia lxml (CVE-2020-27783)

0.4.0 (2019-09-18)
------------------

- Bump requirements
- Require python 3.5


0.3.5 (2019-02-18)
------------------

- Mejora en la detección del encoding de BORME-XML
- No fallar cuando la cabecera Content-Length no esté presente
- Pequeños cambios en los niveles de logging
- download: ajustados los valores por defecto de sleep y threads
- Borrados los checks de python2


0.3.4 (2018-09-24)
------------------

- Nuevo método BormeXML.get_cve_url()


0.3.3 (2018-09-23)
------------------

- is_company(): llama a clean_empresa() y comprueba si contiene la palabra "SOCIEDAD"


0.3.2 (2018-09-23)
------------------

- Actualización de las dependencias
- Tests arreglados
- Nuevo acto mercantil: Adaptación Ley 44/2015
- download_url() ahora reintenta la descarga si hubo un error
- BormeXML.save_to_file() crea el directorio si no existe
- clean_empresa(): quita "EN LIQUIDACION" y "SUCURSAL EN ESPAÑA" del nombre


0.3.1 (2018-05-29)
------------------

- Añadidos más tipos de sociedad
- Borme.from_json: permitir un objeto file como argumento filename


0.3.0 (2018-03-12)
------------------

- Eliminado soporte de Python 2
- Cambios en el formato BORME-JSON
- Nombres de actos repetidos en el mismo anuncio (issue #3)
- Usar requests en lugar de urllib
- Archivo de configuración ~/.bormecfg
- Mejoras en el parser
- Añadidos 4 nuevos actos y 41 cargos directivos
- Borme.to_json ahora permite especificar un path (archivo o directorio) en lugar de solo archivo
- Borme._set_url evita conexión a Internet si existe BORME-XML
- Sociedades y registros tienen su propio módulo
- Funciones de limpieza de datos en bormeparser.clean
- Incluye nombre del R.M. en BORME-JSON
- Cambios menores en los scripts
- Borme.XML devuelve str en lugar de list si solo hay un elemento
- BormeXML.get_provincias

0.2.4 (2016-09-21)
------------------

- BormeXML: get_url_pdfs, get_cves y get_sizes ahora permiten especificar sección y provincia
- Nueva constante ALL_PROVINCIAS en bormeparser.provincia
- Detección de nuevos tipos de sociedades
- Scripts: limpieza, uso de argparse en los scripts, unificación de parámetros
- Mejoras menores en la documentación
- Nuevos campos "version" y "raw_version" en el formato JSON de BORME

0.2.3 (2016-04-26)
------------------

- Mejora en el parser de BORME C

0.2.2 (2016-04-26)
------------------

- Mejoras en el parser de BORME C

0.2.1 (2016-04-25)
------------------

- Corregidos fallos de compatibilidad con Python 2

0.2 (2016-04-25)
----------------

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

0.1.5 (2015-09-25)
------------------

- Añadidos nuevos cargos
- Mejoras en setuptools

0.1.4 (2015-09-24)
------------------

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

0.1.3 (2015-08-08)
------------------

- Fixed missing packages that weren't distributed

0.1.2 (2015-08-07)
------------------

- Fixed UnicodeWarning that caused tests to fail in Python 2

0.1.1 (2015-08-07)
------------------

- setup.py install now installs requirements

0.1 (2015-08-07)
----------------

- First release
- Download and parse BORME PDF files
- Main parser is PyPDF2
- Python 2 and 3 support
- Tests suite
