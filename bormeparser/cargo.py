#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# cargo.py -
# Copyright (C) 2015 Pablo Castellano <pablo@anche.no>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import six


class CARGO:
    PRESIDENTE = 1
    VICEPRESIDENTE = 2
    CONSEJERO = 3
    SECRETARIO = 4
    VICESECRETARIO = 5
    CONS_DEL_MAN = 6
    ADM_UNICO = 7
    MIE_CONS_REC = 8
    PRE_CONS_REC = 9
    SEC_CONS_REC = 10
    ADM_SOLID = 11
    APODERADO = 12
    SOC_PROF = 13
    APO_MAN_SOLI = 14
    APO_MANC = 15
    APO_SOL = 16
    ADM_MANCOM = 17
    CO_DE_MA_SO = 18
    CONS_DEL_SOL = 19
    REPRESENTANTE = 20
    CONS_DELEGADO = 21
    APOD_SOL_MAN = 22
    LIQUISOLI = 23
    LIQUIDADOR = 24
    APODERADO_SOL = 25
    REPR_143_RRM = 26
    AUD_C_CON = 27
    SECRE_NO_CONSEJ = 28
    CONS_DEL_M_S = 29
    VSECR_NO_CONSJ = 30
    AUDITOR = 31
    ADM_CONCURS = 32
    REP_ADM_CONC = 33
    AUD_SUPL = 34
    ADM_CONJUNTO = 35
    ENT_REG_CONT = 36
    ENTIDAD_DEPOSITARIA = 37
    CONSEJERO_DOMINI = 38
    M_COMIT_AUD = 39
    SEC_COMIT_AUD = 40
    PTE_COMIT_AUD = 41
    PRES_COM_CTR = 42
    SECR_COM_CTR = 43
    RLC_PERMA = 44
    LIQUIDADOR_M = 45
    MIEM_COM_CTR = 46
    MIEM_COM_EJ = 47
    SEC_JGPV = 48
    MIEM_JGPV = 49
    PRES_JGPV = 50
    TESORERO = 51
    COMISARIO = 52
    SOCIO_UNICO = 53
    SOCIEDADES_BENEFICIARIAS = 54
    SOCIEDADES_FUSIONADAS = 55

    _keywords = {'Presidente': PRESIDENTE,
                 'Vicepresid': VICEPRESIDENTE,
                 'Consejero': CONSEJERO,
                 'Consj.Domini': CONSEJERO_DOMINI,
                 'Secretario': SECRETARIO,
                 'Vicesecret': VICESECRETARIO,
                 'Cons.Del.Man': CONS_DEL_MAN,
                 'Mie.Cons.Rec': MIE_CONS_REC,
                 'Pre.Cons.Rec': PRE_CONS_REC,
                 'Sec.Cons.Rec': SEC_CONS_REC,
                 'Adm. Unico': ADM_UNICO,
                 'ADM.UNICO': ADM_UNICO,
                 'Adm. Solid.': ADM_SOLID,
                 'ADM.SOLIDAR.': ADM_SOLID,
                 'ADM.CONCURS': ADM_CONCURS,
                 'Adm. Mancom': ADM_MANCOM,
                 'ADM.CONJUNTO': ADM_CONJUNTO,
                 'Apoderado': APODERADO,
                 'APODERADO': APODERADO,
                 'Apo.Man.Soli': APO_MAN_SOLI,
                 'Apo.Manc.': APO_MANC,
                 'APOD.MANCOMU': APO_MANC,
                 'Adm. Mancom.': APO_MANC,
                 'Apo.Sol.': APO_SOL,
                 'APODERAD.SOL': APODERADO_SOL,
                 'APOD.SOL/MAN': APOD_SOL_MAN,
                 'Soc.Prof.': SOC_PROF,
                 'Co.De.Ma.So': CO_DE_MA_SO,
                 'Cons.Del.Sol': CONS_DEL_SOL,
                 'Representan': REPRESENTANTE,
                 'Con.Delegado': CONS_DELEGADO,
                 'Liquidador': LIQUIDADOR,
                 'LiquiSoli': LIQUISOLI,
                 'LiqSolid': LIQUISOLI,
                 'Liquidador M': LIQUIDADOR_M,
                 'REPR.143 RRM': REPR_143_RRM,
                 'CONSEJERO': CONSEJERO,
                 'CONS.DEL.M/S': CONS_DEL_M_S,
                 'CONS. DELEG.': CONS_DELEGADO,
                 'SecreNoConsj': SECRE_NO_CONSEJ,
                 'VsecrNoConsj': VSECR_NO_CONSJ,
                 'Auditor': AUDITOR,
                 'Aud.C.Con.': AUD_C_CON,
                 'Aud.Supl.': AUD_SUPL,
                 'Ent.Reg.Cont': ENT_REG_CONT,
                 'EntidDeposit': ENTIDAD_DEPOSITARIA,
                 'M.Comit.Aud': M_COMIT_AUD,
                 'Sec.Comit.Au': SEC_COMIT_AUD,
                 'Pte.Comit.Au': PTE_COMIT_AUD,
                 'Pres.Com.Ctr': PRES_COM_CTR,
                 'Secr.Com.Ctr': SECR_COM_CTR,
                 'Miem.Com.Ctr': MIEM_COM_CTR,
                 'Miem.Com.Ej.': MIEM_COM_EJ,
                 'R.L.C.Perma.': RLC_PERMA,
                 'Sec.J.G.P.V': SEC_JGPV,
                 'Miem.J.G.P.V': MIEM_JGPV,
                 'Pres.J.G.P.V': PRES_JGPV,
                 'Tesorero': TESORERO,
                 'REP.ADM.CONC': REP_ADM_CONC,
                 'Comisario': COMISARIO,
                 'Socio único': SOCIO_UNICO,

                 # hack
                 'Sociedades beneficiarias': SOCIEDADES_BENEFICIARIAS,
                 'Sociedades fusionadas': SOCIEDADES_FUSIONADAS,
                 }
    KEYWORDS = list(six.viewkeys(_keywords))

    @staticmethod
    def from_string(string):
        return CARGO._keywords[string]
