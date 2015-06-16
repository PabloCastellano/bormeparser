#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import json
import re
import sys
import getopt
import time

try:
    from PyPDF2 import PdfFileWriter, PdfFileReader
    logging.info('Using PyPDF2')
    print('Using PyPDF2')
except ImportError:
    from pyPdf import PdfFileWriter, PdfFileReader
    logging.info('Using deprecated pyPdf')
    print('Using PyPDF2')

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams

from bormeparser.acto import ACTOS
from bormeparser.borme import BormeActo

CROP_FIRST = (0.08196721311475409, 0.26981300089047194, 0.09079445145018916, 0.0)
CROP_MIDDLE = (0.0832282471626734, 0.11308993766696349, 0.08953341740226986, 0.03294746215494212)
CROP_LAST = (0.0832282471626734, 0.11308993766696349, 0.08953341740226986, 0.053428317008014245)

# OR de las palabras clave con argumentos
RE_ARG_KEYWORDS = '(%s)' % '|'.join(ACTOS.ARG_KEYWORDS)
# OR de todas las palabras clave, "non grouping"
RE_ALL_KEYWORDS_NG = '(?:%s|%s|%s|%s)' % ('|'.join(ACTOS.ARG_KEYWORDS), '|'.join(ACTOS.COLON_KEYWORDS), '|'.join(ACTOS.NOARG_KEYWORDS), ACTOS.ENDING_KEYWORDS[0])
# OR de las palabras clave sin argumentos
RE_NOARG_KEYWORDS = '(%s)' % '|'.join(ACTOS.NOARG_KEYWORDS)
# OR de las palabras clave con argumentos seguidas por :
RE_COLON_KEYWORDS = '(%s)' % '|'.join(ACTOS.COLON_KEYWORDS)
RE_ENDING_KEYWORD = '(%s)' % ACTOS.ENDING_KEYWORDS[0]

# Cargos
"""
RE_CARGOS_KEYWORD = '(%s)' % '|'.join(ACTOS.CARGOS_KEYWORD)
RE_CARGOS_KEYWORD_NG = '(?:\.\s*%s|$)' % '|'.join(RE_CARGOS_KEYWORD) # MAL, FIX, pero funciona RE_...
for match in re.finditer(RE_CARGOS_KEYWORD + ':\s+(.*?)' + RE_CARGOS_KEYWORD_NG, str1):
    print match.group(1), match.group(2)
"""

REGEX1 = re.compile('^(\d+) - (.*?)\.\s*' + RE_ALL_KEYWORDS_NG)
REGEX2 = re.compile('(?=' + RE_ARG_KEYWORDS + '\.\s+(.*?)\.\s*' + RE_ALL_KEYWORDS_NG + ')')
REGEX3 = re.compile(RE_COLON_KEYWORDS + ':\s+(.*?)\.\s*' + RE_ALL_KEYWORDS_NG)
REGEX4 = re.compile(RE_ENDING_KEYWORD + '\.\s+(.*)\.\s*')
REGEX5 = re.compile(RE_NOARG_KEYWORDS + '\.')


CROP_FIRST = (0.08196721311475409, 0.26981300089047194, 0.09079445145018916, 0.0)
CROP_MIDDLE = (0.0832282471626734, 0.11308993766696349, 0.08953341740226986, 0.03294746215494212)
CROP_LAST = (0.0832282471626734, 0.11308993766696349, 0.08953341740226986, 0.053428317008014245)


def _crop_page(page, crop, rotate):
    # Note that the coordinate system is up-side down compared with Qt.
    x0, y0 = page.mediaBox.lowerLeft
    x1, y1 = page.mediaBox.upperRight
    x0, y0, x1, y1 = float(x0), float(y0), float(x1), float(y1)
    x0, x1 = x0 + crop[0] * (x1 - x0), x1 - crop[2] * (x1 - x0)
    y0, y1 = y0 + crop[3] * (y1 - y0), y1 - crop[1] * (y1 - y0)
    page.mediaBox.lowerLeft = (x0, y0)
    page.mediaBox.upperRight = (x1, y1)
    # Update CropBox as well
    page.cropBox.lowerLeft = (x0, y0)
    page.cropBox.upperRight = (x1, y1)
    if rotate != 0:
        page.rotateClockwise(rotate)


def crop_file(filename_in, filename_out, rewrite=False):
    """
        Crop file according to BORME PDF format

        filename_in:
        filename_out:
        rewrite:
    """

    if os.path.exists(filename_out) and not rewrite:
        logging.info('Skipping file %s already exists and rewriting is disabled!' % filename_out)
        return False

    # PyPDF2 bug?
    #pdf_fp = open(filename_in, "rb")
    #reader = PdfFileReader(pdf_fp)
    reader = PdfFileReader(open(filename_in, "rb"))
    writer = PdfFileWriter()
    num_pages = reader.getNumPages()

    # cabecera
    page = reader.getPage(0)
    # (x0, x1, y0, y1)
    _crop_page(page, CROP_FIRST, False)
    writer.addPage(page)

    for i in range(1, num_pages - 1):
        page = reader.getPage(i)
        _crop_page(page, CROP_MIDDLE, False)
        writer.addPage(page)

    # borde final
    page = reader.getPage(num_pages - 1)
    _crop_page(page, CROP_LAST, False)
    writer.addPage(page)

    #pdf_fp.close()

    output_fp = open(filename_out, 'wb')
    writer.write(output_fp)
    #output_fp.close()
    #with open(filename_out, 'wb') as fp:
    #    writer.write(fp)

    return True


def clean_file(filename_in, filename_out, rewrite=False):
    """
        Parse file according to BORME PDF format

        filename:
        filenameOut:
    """

    if os.path.isdir(filename_out):
        filename_out = os.path.join(filename_out, os.path.basename(filename_in))

    if os.path.exists(filename_out) and not rewrite:
        logging.info('Skipping file %s already exists and rewriting is disabled!' % filename_out)
        return False

    outfp = open(filename_out, 'w')
    fp = open(filename_in, 'r')

    # Al comienzo de una página nueva, el parser de PDF a texto añade el carácter 0x0c (^L)
    # y hace que no funcionen las expresiones regulares en estos casos.
    content = fp.read()
    content = re.sub(r"^\x0c(\d+)", "\\1", content, flags=re.M)
    content = re.sub(r"^\x0a\x0c(?!\d+)", "", content, flags=re.M)

    outfp.write(content)

    fp.close()
    outfp.close()

    return True


def convert_to_text_file(filename_in, filename_out, rewrite=False):
    """
        Parse file according to BORME PDF format

        filename:
        filenameOut:
    """

    if os.path.isdir(filename_out):
        filename_out = os.path.join(filename_out, os.path.basename(filename_in))

    if os.path.exists(filename_out) and not rewrite:
        logging.info('Skipping file %s already exists and rewriting is disabled!' % filename_out)
        return False

    # conf
    codec = 'utf-8'
    laparams = LAParams()
    imagewriter = None
    pagenos = set()
    maxpages = 0
    password = ''
    rotation = 0

    # <LAParams: char_margin=2.0, line_margin=0.5, word_margin=0.1 all_texts=False>
    laparams.detect_vertical = True
    laparams.all_texts = False
    laparams.char_margin = 2.0
    laparams.line_margin = 0.5
    laparams.word_margin = 0.1

    caching = True
    rsrcmgr = PDFResourceManager(caching=caching)
    outfp = open(filename_out, 'w')
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams, imagewriter=imagewriter)
    fp = open(filename_in, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # https://github.com/euske/pdfminer/issues/72
    #page = PDFPage()
    #PDFPage.cropbox =

    # y esto?
    for page in PDFPage.get_pages(fp, pagenos,
                                  maxpages=maxpages, password=password,
                                  caching=caching, check_extractable=True):
        page.rotate = (page.rotate + rotation) % 360
        interpreter.process_page(page)

    fp.close()
    device.close()
    outfp.close()
    return True


def _parse_line(trozo):

    data = {}

    def save_field(content):
        logging.debug('Guardando %s', content)
        data[content[0]] = content[1]

    tr2_ = trozo.replace('\n', ' ').replace('  ', ' ')
    logging.debug(tr2_)

    m = REGEX1.match(tr2_)

    save_field(('ID', m.group(1)))
    save_field(('Nombre', m.group(2)))

    for match in REGEX2.finditer(tr2_):
        save_field((match.group(1), match.group(2)))

    for match in REGEX3.finditer(tr2_):
        save_field((match.group(1), match.group(2)))

    for match in REGEX4.finditer(tr2_):
        save_field((match.group(1), match.group(2)))

    for match in REGEX5.finditer(tr2_):
        save_field((match.group(1), 'X'))
    return data


def parse_file(filename_in, filename_out, rewrite=False):
    """
        Parse file according to BORME PDF format

        filename:
        filenameOut:
    """

    had_warning = False
    jsondata = []
    results = {'error': 0, 'skip': 0, 'ok': 0, 'warning': 0}

    if os.path.exists(filename_out) and not rewrite:
        logging.info('Skipping file %s already exists and rewriting is disabled!' % filename_out)
        results['skip'] += 1
        return False

    fp = open(filename_in, 'r')
    text = fp.read()
    fp.close()

    outfp = open(filename_out, 'w')

    for trozo in text.split('.\n\n'):
        trozo += '.'

        try:
            data =_parse_line(trozo)
            logging.debug('###########')
            logging.debug('Keys: %s total: %d', data.keys(), len(data))
            logging.debug('%s', data)
            jsondata.append(data)
            logging.debug('###########')
        except Exception as e:
            logging.error(e)
            had_warning = True
            logging.warning('###########')
            logging.warning('SKIPPING. Invalid data found:')
            logging.warning(trozo)
            logging.warning('###########')
            results['error'] += 1

    #outfp.write(json.dumps(self.jsondata))
    outfp.write(json.dumps(jsondata, sort_keys=True, indent=4))
    outfp.close()

    if had_warning:
        results['error'] += 1

    results['ok'] += 1
    return True


def parse_file_actos(filename_in, rewrite=False):
    """
        Parse file according to BORME PDF format

        filename:
        filenameOut:
    """

    had_warning = False
    actos = {}
    results = {'error': 0, 'skip': 0, 'ok': 0, 'warning': 0}

    fp = open(filename_in, 'r')
    text = fp.read()
    fp.close()

    for trozo in text.split('.\n\n'):
        trozo += '.'

        try:
            data =_parse_line(trozo)
            logging.debug('###########')
            logging.debug('Keys: %s total: %d', data.keys(), len(data))
            logging.debug('%s', data)
            acto_id = int(data.pop('ID'))
            acto_empresa = data.pop('Nombre')
            actos[acto_id] = BormeActo(acto_id, acto_empresa, data)
            logging.debug('###########')
        except Exception as e:
            logging.error(e)
            had_warning = True
            logging.warning('###########')
            logging.warning('SKIPPING. Invalid data found:')
            logging.warning(trozo)
            logging.warning('###########')
            results['error'] += 1

    if had_warning:
        results['error'] += 1

    results['ok'] += 1
    return actos, results