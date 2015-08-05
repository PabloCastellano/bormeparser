#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from bormeparser.borme import Borme, BormeAnuncio
from bormeparser.regex import regex_fecha
from bormeparser.download import get_url_pdf
from bormeparser import SECCION, PROVINCIA


class BormeParserBackend(object):
    def __init__(self, filename):

        if not os.path.isfile(filename):
            raise IOError

        self.filename = filename

    def parse(self):
        anuncios = self._parse()
        bormeanuncios = []
        for id_anuncio in anuncios.keys():
            if not isinstance(id_anuncio, int):
                continue
            data = anuncios[id_anuncio]
            a = BormeAnuncio(id_anuncio, data['Empresa'], data['Actos'])
            bormeanuncios.append(a)

        fecha = regex_fecha(anuncios['borme_fecha'])
        # FIXME: provincia, seccion objects
        seccion = SECCION.from_borme(anuncios['borme_seccion'], anuncios['borme_subseccion'])
        provincia = PROVINCIA.from_title(anuncios['borme_provincia'])
        url = get_url_pdf(fecha, seccion, provincia)
        return Borme(fecha, seccion, provincia, anuncios['borme_num'], anuncios['borme_cve'], bormeanuncios, url=url, filename=self.filename)

    def _parse(self):
        """
        :return: diccionario con key= id del acto y value {'Empresa': str, 'Actos': dict}
        """
        raise NotImplementedError

    def parse_actos(self):
        self._parse_actos()

    def _parse_actos(self):
        raise NotImplementedError
