#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import requests

import bormeparser.backends

from .borme import Borme
import datetime

# backends
# TODO: Dynamic import
DEFAULT_PARSER = bormeparser.backends.parser1

# parse: url, filename (string)
def parse(data):

    if os.path.isfile(data):
        # pasar file(data)
        parser = bormeparser.backends.Parser1(data)
        actos = parser.parse_actos()
    elif data.startswith('http'):
        content = requests.get(data).read()
        parser = bormeparser.backends.Parser1(content)
        actos = parser.parse_actos()
    else:
        raise ValueError

    return Borme(datetime.date(1970, 1, 1), 'DUMMY', 'DUMMY', actos)
