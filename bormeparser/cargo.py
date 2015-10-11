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
    PRESIDENTE_COMISION_CONTROL = 42
    SECRETARIO_COMISION_CONTROL = 43
    RLC_PERMA = 44
    LIQUIDADOR_M = 45
    MIEMBRO_COMISION_CONTROL = 46
    MIEM_COM_EJ = 47
    SEC_JGPV = 48
    MIEM_JGPV = 49
    PRES_JGPV = 50
    TESORERO = 51
    COMISARIO = 52
    SOCIO_UNICO = 53
    SOCIEDADES_BENEFICIARIAS = 54
    SOCIEDADES_FUSIONADAS = 55
    GERENTE = 56
    LIQUIDADOR_UNICO = 57
    CONS_DEL_C_R = 58
    ENTIDAD_GESTORA = 59
    AUDITOR_TITU = 60
    AUDITOR_CUENTAS = 61
    DIRECTOR_GENERAL = 62
    MIEMBRO_JUNTA_DIRECTIVA = 63
    SECRETARIO_JUNTA_DIRECTIVA = 64
    SOCIO = 65
    COMS_DEL_INV = 66  # Comisario del inv...?
    PRE_COMS_D_I = 67  # Presidente coms del inv...?
    S_N_C_C_D_I = 68  # Secretario no consejero Coms del inv?
    VS_N_C_C_D_I = 69  # Vicesecretario no consejero coms del inv?
    NO_DEFINIDO = 70
    LETRADO_ASESOR = 71
    EXP_IND = 72  # Experto independiente?
    MIEMBRO_COM_LIQ = 73
    PRESIDENTE_COM_LIQ = 74
    SECRETARIO_COM_LIQ = 75
    GER_COM_GER = 76  #
    ADMINISTRADOR = 77
    VOCAL_JUNTA_DIRECTIVA = 78
    VOCAL_SECUNDARIO_JUNTA_DIRECTIVA = 79
    VICEPRESIDENTE_JUNTA_DIRECTIVA = 80
    VICEPRESIDENTE_SEGUNDO_JUNTA_DIRECTIVA = 81
    TESORERO_JUNTA_DIRECTIVA = 82

    _keywords = {'Presidente': PRESIDENTE,
                 'Vicepresid.': VICEPRESIDENTE,
                 'VICEPRESIDEN': VICEPRESIDENTE,
                 'Consejero': CONSEJERO,
                 'Consj.Domini': CONSEJERO_DOMINI,
                 'Secretario': SECRETARIO,
                 'SECRETARIO': SECRETARIO,
                 'Vicesecret.': VICESECRETARIO,
                 'Cons.Del.Man': CONS_DEL_MAN,
                 'Mie.Cons.Rec': MIE_CONS_REC,
                 'Pre.Cons.Rec': PRE_CONS_REC,
                 'Sec.Cons.Rec': SEC_CONS_REC,
                 'Adm. Unico': ADM_UNICO,
                 'ADM.UNICO': ADM_UNICO,
                 'Admin.Unico': ADM_UNICO,
                 'Adm. Solid.': ADM_SOLID,
                 'ADM.SOLIDAR.': ADM_SOLID,
                 'Admin.Solid': ADM_SOLID,
                 'ADM.CONCURS.': ADM_CONCURS,
                 'Adm. Mancom': ADM_MANCOM,
                 'Admin.Manc': ADM_MANCOM,
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
                 'CONS. DELEG.': CONS_DELEGADO,
                 'Cons.Delegad': CONS_DELEGADO,
                 'Liquidador': LIQUIDADOR,
                 'LIQUIDADOR': LIQUIDADOR,
                 'LiquiSoli': LIQUISOLI,
                 'LiqSolid': LIQUISOLI,
                 'Liquidador M': LIQUIDADOR_M,
                 'REPR.143 RRM': REPR_143_RRM,
                 'CONSEJERO': CONSEJERO,
                 'CONS.DEL.M/S': CONS_DEL_M_S,
                 'SecreNoConsj': SECRE_NO_CONSEJ,
                 'SECR.NO CONS': SECRE_NO_CONSEJ,
                 'VsecrNoConsj': VSECR_NO_CONSJ,
                 'V-SEC NO CON': VSECR_NO_CONSJ,
                 'Auditor': AUDITOR,
                 'Aud.C.Con.': AUD_C_CON,
                 'Aud.Supl.': AUD_SUPL,
                 'Ent.Reg.Cont': ENT_REG_CONT,
                 'EntidDeposit': ENTIDAD_DEPOSITARIA,
                 'ENT.DEPOSIT.': ENTIDAD_DEPOSITARIA,
                 'M.Comit.Aud': M_COMIT_AUD,
                 'Sec.Comit.Au': SEC_COMIT_AUD,
                 'Pte.Comit.Au': PTE_COMIT_AUD,
                 'Pte. C. Aud.': PTE_COMIT_AUD,
                 'Pres.Com.Ctr': PRESIDENTE_COMISION_CONTROL,
                 'Secr.Com.Ctr': SECRETARIO_COMISION_CONTROL,
                 'Miem.Com.Ctr': MIEMBRO_COMISION_CONTROL,
                 'MRO.COMS.CTR': MIEMBRO_COMISION_CONTROL,
                 'Miem.Com.Ej.': MIEM_COM_EJ,
                 'R.L.C.Perma.': RLC_PERMA,
                 'Sec.J.G.P.V': SEC_JGPV,
                 'Miem.J.G.P.V': MIEM_JGPV,
                 'Pres.J.G.P.V': PRES_JGPV,
                 'Tesorero': TESORERO,
                 'REP.ADM.CONC': REP_ADM_CONC,
                 'Comisario': COMISARIO,
                 'Comis.Contro': COMISARIO,
                 'Socio único': SOCIO_UNICO,
                 'Gerente': GERENTE,
                 'LiqUnico': LIQUIDADOR_UNICO,
                 'Cons.Del.C.R': CONS_DEL_C_R,
                 'Ent. Gestora': ENTIDAD_GESTORA,
                 'ENTI.GESTORA': ENTIDAD_GESTORA,
                 'Auditor Titu': AUDITOR_TITU,
                 'AUDIT.CUENT.': AUDITOR_CUENTAS,
                 'Dir. General': DIRECTOR_GENERAL,
                 'Miem.J.Dir.': MIEMBRO_JUNTA_DIRECTIVA,
                 'Scrt.J.Dir.': SECRETARIO_JUNTA_DIRECTIVA,
                 'SEC.JTA.DIRE': SECRETARIO_JUNTA_DIRECTIVA,
                 'Socio': SOCIO,
                 'COMS.DEL.INV': COMS_DEL_INV,
                 'PRE.COMS.D.I': PRE_COMS_D_I,
                 'S.N.C.C.D.I.': S_N_C_C_D_I,
                 'VS.N.C.C.D.I': VS_N_C_C_D_I,
                 'No definido:': NO_DEFINIDO,  #
                 'L. Asesor': LETRADO_ASESOR,
                 'Exp.Ind.': EXP_IND,
                 'Mmbr.Com.Liq': MIEMBRO_COM_LIQ,
                 'Pres.Com.Liq': PRESIDENTE_COM_LIQ,
                 'Secr.Com.Liq': SECRETARIO_COM_LIQ,
                 'Ger.Com.Ger': GER_COM_GER,
                 'ADMINISTR.': ADMINISTRADOR,
                 'VOCAL JTA.DI': VOCAL_JUNTA_DIRECTIVA,
                 'VOC.S.JTA.DI': VOCAL_SECUNDARIO_JUNTA_DIRECTIVA,
                 'V-PRE.JTA.DI': VICEPRESIDENTE_JUNTA_DIRECTIVA,
                 'V-PR.S.JTA.D': VICEPRESIDENTE_SEGUNDO_JUNTA_DIRECTIVA,
                 'TESOR.JTA.DI': TESORERO_JUNTA_DIRECTIVA,


                 # hack
                 'Sociedades beneficiarias': SOCIEDADES_BENEFICIARIAS,
                 'Sociedades fusionadas': SOCIEDADES_FUSIONADAS,
                 }
    KEYWORDS = list(six.viewkeys(_keywords))

    @staticmethod
    def from_string(string):
        return CARGO._keywords[string]
