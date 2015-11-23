#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
from lxml import etree

from .exceptions import BormeDoesntExistException
from .parser import parse as parse_borme
from threading import Thread

try:
    # Python 3
    from queue import Queue
    from urllib import request
except ImportError:
    from Queue import Queue
    import urllib as request

import logging
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
logger.addHandler(ch)
logger.setLevel(logging.WARN)

# URLs

# DON'T REWRITE BY DEFAULT
# TODO: comprobar bytes

# Falla https
# TODO: boe.gob.es es un mirror? Resuelve a una IP distinta.
#BORME_XML_URL = "https://www.boe.es/diario_borme/xml.php?id=BORME-S-"
BORME_XML_URL = "http://www.boe.es/diario_borme/xml.php?id=BORME-S-%d%02d%02d"
BORME_PDF_URL = "http://boe.es/borme/dias/%d/%02d/%02d/pdfs/BORME-%s-%d-%s-%s.pdf"
URL_BASE = 'http://www.boe.es'

# Download threads
THREADS = 4


# date = (year, month, date) or datetime.date
# filename = path to filename or just filename
def download_xml(date, filename):
    url = get_url_xml(date)
    downloaded = download_url(url, filename)
    return downloaded


def download_pdfs(date, path, provincia=None, seccion=None):
    """ Descarga BORMEs PDF de las provincia, la seccion y la fecha indicada """
    urls = get_url_pdfs(date, provincia=provincia, seccion=seccion)
    files = download_urls(urls, path)
    return True, files


# date = (year, month, date) or datetime.date
# seccion = ('A', 'B', 'C') or SECCION.A, SECCION.B, ...
# province = class PROVINCIA: PROVINCIA.MALAGA, PROVINCIA.MADRID, ...
def download_pdf(date, filename, seccion, provincia, parse=False):
    """ Descarga BORME PDF de la provincia, la seccion y la fecha indicada """
    url = get_url_pdf(date, seccion, provincia)
    downloaded = download_url(url, filename)

    if downloaded:
        logger.debug('Downloaded %s' % filename)
    else:
        return False

    if parse:
        return parse_borme(filename)

    return True


# No se puede porque van numerados. Ademas de la fecha, el tipo y la provincia necesitariamos saber el numero de
# borme del año. Lo unico que se podria hacer es bajar el xml y ahi ver la url
# date = (year, month, date) or datetime.date
# seccion = ('A', 'B', 'C') or class SECCION
# province = class PROVINCIA
# "http://boe.es/borme/dias/2015/06/01/pdfs/BORME-A-2015-101-29.pdf"
def get_url_pdf(date, seccion, provincia):
    if isinstance(date, tuple):
        date = datetime.date(year=date[0], month=date[1], day=date[2])

    url = get_url_xml(date)
    nbo = get_nbo_from_xml(url)
    return BORME_PDF_URL % (date.year, date.month, date.day, seccion, date.year, nbo, provincia.code)


def get_url_pdf_from_xml(date, seccion, provincia, xml_path):
    if isinstance(date, tuple):
        date = datetime.date(year=date[0], month=date[1], day=date[2])

    nbo = get_nbo_from_xml(xml_path)
    return BORME_PDF_URL % (date.year, date.month, date.day, seccion, date.year, nbo, provincia.code)


def get_nbo_from_xml(xml_path):
    """ Número de Boletín Oficial """
    tree = etree.parse(xml_path)

    if tree.getroot().tag != 'sumario':
        raise BormeDoesntExistException

    return tree.xpath('//sumario/diario')[0].attrib['nbo']


def get_url_pdfs_provincia(date, provincia):
    """ Obtiene las URLs para descargar los BORMEs de la provincia y fecha indicada """
    url = get_url_xml(date)
    tree = etree.parse(url)

    if tree.getroot().tag != 'sumario':
        raise BormeDoesntExistException

    urls = {}
    for item in tree.xpath('//sumario/diario/seccion/emisor/item'):
        prov = item.xpath('titulo')[0].text
        if prov != provincia:
            continue
        url = URL_BASE + item.xpath('urlPdf')[0].text
        seccion = item.getparent().getparent().get('num')
        urls[seccion] = url

    return urls


def get_url_pdfs_seccion(date, seccion):
    """ Obtiene las URLs para descargar los BORMEs de la seccion y fecha indicada """
    url = get_url_xml(date)
    tree = etree.parse(url)

    if tree.getroot().tag != 'sumario':
        raise BormeDoesntExistException

    urls = {}
    for item in tree.xpath('//sumario/diario/seccion[@num="%s"]/emisor/item' % seccion):
        provincia = item.xpath('titulo')[0].text
        url = URL_BASE + item.xpath('urlPdf')[0].text
        urls[provincia] = url

    return urls


def get_url_pdfs(date, seccion=None, provincia=None):
    if seccion and not provincia:
        urls = get_url_pdfs_seccion(date, seccion)
    elif provincia and not seccion:
        urls = get_url_pdfs_provincia(date, provincia)
    elif provincia and seccion:
        raise NotImplementedError
    else:
        raise AttributeError('You must specifiy either provincia or seccion or both')
    return urls


# date = (year, month, date) or datetime.date
# "http://www.boe.es/diario_borme/xml.php?id=BORME-S-20150601"
def get_url_xml(date):
    """ Obtiene el archivo XML que contiene las URLs de los BORMEs del dia indicado """
    if isinstance(date, tuple):
        date = datetime.date(year=date[0], month=date[1], day=date[2])

    return BORME_XML_URL % (date.year, date.month, date.day)


# TODO: FileExistsError (subclass de OSError)
def download_url(url, filename=None):
    logger.info('Downloading URL: %s' % url)
    if os.path.exists(filename):
        logger.warning('%s already exists!' % os.path.basename(filename))
        return False

    local_filename, headers = request.urlretrieve(url, filename)
    content_length = headers['content-length']
    logger.debug("%.2f KB" % (int(content_length) / 1024.0))

    return True, local_filename


def download_urls(urls, path):
    """ Descarga las urls a path indicado """
    files = []
    for url in urls.values():
        filename = url.split('/')[-1]
        full_path = os.path.join(path, filename)
        downloaded = download_url(url, full_path)

        if downloaded:
            files.append(full_path)
            logger.info('Downloaded %s' % filename)

        #assert os.path.exists(filepdf)
        #assert os.path.getsize(filepdf) == int(url.attrib['szBytes'])
    return files


def download_urls_multi(urls, path, threads=THREADS):
    """ Descarga las urls a path indicado (verisón multihilo) """

    q = Queue()
    files = []

    for i in range(THREADS):
        t = ThreadDownloadUrl(i, q, files)
        t.setDaemon(True)
        t.start()

    for url in urls.values():
        filename = url.split('/')[-1]
        full_path = os.path.join(path, filename)
        q.put((url, full_path))

    q.join()
    return files


class ThreadDownloadUrl(Thread):
    """Threaded Url Grab"""
    def __init__(self, thread_id, queue, files):
        super(ThreadDownloadUrl, self).__init__()
        self.thread_id = thread_id
        self.queue = queue
        self.files = files

    def run(self):
        while True:
            url, full_path = self.queue.get()
            downloaded = download_url(url, full_path)

            if downloaded:
                self.files.append(full_path)
                logger.info('Downloaded %s' % os.path.basename(full_path))

            self.queue.task_done()
