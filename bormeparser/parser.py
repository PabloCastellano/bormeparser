#!/usr/bin/env python
# -*- coding: utf-8 -*-

import importlib
import os
import requests

# backends
DEFAULT_PARSER = ('bormeparser.backends.pypdf2.parser', 'PyPDF2Parser')


# parse: url, filename (string)
def parse(data):
    module = importlib.import_module(DEFAULT_PARSER[0])
    parser = getattr(module, DEFAULT_PARSER[1])
    if os.path.isfile(data):
        # FIXME: pasar open(data)
        borme = parser(data).parse()
    elif data.startswith('http'):
        # TODO
        content = requests.get(data).read()
        borme = parser(data).parse()
        #actos = parser.parse_actos()
    else:
        raise FileNotFoundError(data)

    return borme
