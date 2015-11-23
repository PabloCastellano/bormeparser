#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import os

try:
    # Python 3
    from urllib import request
except ImportError:
    import urllib as request

# backends
DEFAULT_PARSER = ('bormeparser.backends.pypdf2.parser', 'PyPDF2Parser')


# parse: url, filename (string)
def parse(data):
    module = importlib.import_module(DEFAULT_PARSER[0])
    parser = getattr(module, DEFAULT_PARSER[1])
    if os.path.isfile(data):
        borme = parser(data).parse()
    elif data.startswith('http'):
        # TODO
        #content = request.urlopen(data).read()
        borme = parser(data).parse()
    else:
        raise FileNotFoundError(data)

    return borme
