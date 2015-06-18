#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from bormeparser.borme import Borme, BormeActo
import datetime

class BormeParserBackend(object):
    def __init__(self, filename):

        if not os.path.isfile(filename):
            raise IOError

        self.filename = filename

    def parse(self):
        actos = self._parse()
        bormeactos = []
        for id_acto in actos.keys():
            data = actos[id_acto]
            a = BormeActo(id_acto, data['Empresa'], data['Actos'])
            bormeactos.append(a)
        # FIXME
        return Borme(datetime.date(1970, 1, 1), 'DUMMY', 'DUMMY', bormeactos)

    def _parse(self):
        """
        :return: diccionario con key= id del acto y value {'Empresa': str, 'Actos': dict}
        """
        raise NotImplementedError

    def parse_actos(self):
        self._parse_actos()

    def _parse_actos(self):
        raise NotImplementedError
