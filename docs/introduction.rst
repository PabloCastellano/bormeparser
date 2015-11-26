Introducción
============

**bormeparser** es una librería de Python para parsear los archivos del BORME (Boletín Oficial del Registro Mercantil en España).

Qué es BORME
------------

El **Boletín Oficial del Registro Mercantil** es un documento publicado diariamente por el Registro Mercantil Central (RMC)
en España que contiene un listado de las últimas sociedades creadas y disueltas así como otros datos que las empresas
están obligadas a comunicar.

La librería aprovecha que desde la aprobación de `esta ley`_,
desde el año 2009 el BORME se publica también en formato electrónico con la misma validez que su versión en papel.

Los BORMEs se publican en https://boe.es/diario_borme/.

Desgraciadamente debido al acuerdo actual con el Registro Mercantil, no pueden publicar todos los datos en un formato
útil y reutilizable como XML o JSON y los datos más interesantes están solo disponibles en los archivos PDF.

Puedes leer más sobre ello en:

- Wikipedia: `https://es.wikipedia.org/wiki/Boletín_Oficial_del_Registro_Mercantil`_

.. _esta ley: https://www.boe.es/buscar/doc.php?id=BOE-A-2008-19826
.. _https://es.wikipedia.org/wiki/Boletín_Oficial_del_Registro_Mercantil: https://es.wikipedia.org/wiki/Boletín_Oficial_del_Registro_Mercantil
