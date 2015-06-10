#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import requests
from lxml import etree

from .exceptions import BormeDoesntExistException

# URLs

# DON'T REWRITE BY DEFAULT
# TODO: comprobar bytes

# Falla https
#BORME_XML_URL = "https://www.boe.es/diario_borme/xml.php?id=BORME-S-"
BORME_XML_URL = "http://www.boe.es/diario_borme/xml.php?id=BORME-S-%d%02d%02d"
BORME_PDF_URL = "http://boe.es/borme/dias/%d/%02d/%02d/pdfs/BORME-%s-%d-%s-%s.pdf"
URL_BASE = 'http://www.boe.es'

# http request timeout, default is 5 seconds
TIMEOUT = 5

# date = (year, month, date) or datetime.date
# filename = path to filename or just filename
def download_xml(date, filename):
    url = get_url_xml(date)
    downloaded = download_url(url, filename)
    return downloaded

# TODO: def download_pdfs(date, path, provincia)

def download_pdfs(date, path, seccion):
    url = get_url_xml(date)
    tree = etree.parse(url)

    for url in tree.xpath('//sumario/diario/seccion[@num="%s"]/emisor/item/urlPdf' % seccion):
        filename = url.text.split('/')[-1]
        full_path = os.path.join(path, filename)
        full_url = URL_BASE + url.text
        downloaded = download_url(full_url, full_path)

        if not downloaded:
            print("ERROR downloading %s" % url.text)
            continue

        #assert os.path.exists(filepdf)
        #assert os.path.getsize(filepdf) == int(url.attrib['szBytes'])

    return True

# date = (year, month, date) or datetime.date
# seccion = ('A', 'B', 'C') or class SECCION
# province = class PROVINCIA
def download_pdf(date, filename, seccion, provincia):
    url = get_url_pdf(date, seccion, provincia)
    downloaded = download_url(url, filename)

    return downloaded


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
    tree = etree.parse(url)

    if tree.getroot().tag != 'sumario':
        raise BormeDoesntExistException

    nbo = tree.xpath('//sumario/diario')[0].attrib['nbo']

    return BORME_PDF_URL % (date.year, date.month, date.day, seccion, date.year, nbo, provincia)


def get_url_pdfs(date, seccion):
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


# date = (year, month, date) or datetime.date
# "http://www.boe.es/diario_borme/xml.php?id=BORME-S-20150601"
def get_url_xml(date):
    if isinstance(date, tuple):
        date = datetime.date(year=date[0], month=date[1], day=date[2])

    return BORME_XML_URL % (date.year, date.month, date.day)


# TODO: FileExistsError (subclass de OSError)
def download_url(url, filename, timeout=TIMEOUT):
    if os.path.exists(filename):
        return False

    r = requests.get(url, stream=True, timeout=timeout)
    cl = r.headers.get('content-length')
    print("%.2f KB" % (int(cl) / 1024.0))

    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(8192):
            fd.write(chunk)

    return True
