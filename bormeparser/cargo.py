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
    CONSEJERO_DELEGADO_MANCOMUNADO = 6
    ADM_UNICO = 7
    MIEMBRO_CONSEJO_RECTOR = 8
    PRESIDENTE_CONSEJO_RECTOR = 9
    SECRETARIO_CONSEJO_RECTOR = 10
    ADM_SOLID = 11
    APODERADO = 12
    SOC_PROF = 13
    APODERADO_MANCOMUNADO_SOLIDARIO = 14
    APODERADO_MANCOMUNADO = 15
    APODERADO_SOLIDARIO = 16
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
    AUDITOR_CUENTAS_CONSOLIDADAS = 27
    SECRETARIO_NO_CONSEJ = 28
    CONS_DEL_M_S = 29
    VICESECRETARIO_NO_CONSJ = 30
    AUDITOR = 31
    ADM_CONCURS = 32
    REP_ADM_CONC = 33
    AUDITOR_SUPL = 34
    ADM_CONJUNTO = 35
    ENT_REG_CONT = 36
    ENTIDAD_DEPOSITARIA = 37
    CONSEJERO_DOMINI = 38
    MIEMBRO_COMIT_AUD = 39
    SECRETARIO_COMIT_AUD = 40
    PRESIDENTE_COMIT_AUD = 41
    PRESIDENTE_COMISION_CONTROL = 42
    SECRETARIO_COMISION_CONTROL = 43
    RLC_PERMA = 44  # Representante
    LIQUIDADOR_MANCOMUNADO = 45
    MIEMBRO_COMISION_CONTROL = 46
    MIEMBRO_COMISION_EJECUTIVA = 47
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
    PRESIDENTE_COMS_D_I = 67  # Presidente coms del inv...?
    S_N_C_C_D_I = 68  # Secretario no consejero Coms del inv?
    VS_N_C_C_D_I = 69  # Vicesecretario no consejero coms del inv?
    NO_DEFINIDO = 70  # ?
    LETRADO_ASESOR = 71
    EXP_IND = 72  # Experto independiente?
    MIEMBRO_COM_LIQ = 73
    PRESIDENTE_COM_LIQ = 74
    SECRETARIO_COM_LIQ = 75
    GER_COM_GER = 76  # ?
    ADMINISTRADOR = 77
    VOCAL_JUNTA_DIRECTIVA = 78
    VOCAL_SECUNDARIO_JUNTA_DIRECTIVA = 79
    VICEPRESIDENTE_JUNTA_DIRECTIVA = 80
    VICEPRESIDENTE_SEGUNDO_JUNTA_DIRECTIVA = 81
    TESORERO_JUNTA_DIRECTIVA = 82
    DIRECTOR = 83
    DEF_PARTICIP = 84  # ?
    ADM_JUDICIAL = 85
    ADM_SUPL = 86
    APODERADO_D_GENERAL = 87
    MIEMBRO_COMITE_INV = 88
    APOD_D_GENERAL = 89
    COM_AUDIT = 90  # Miem. Com. Audit.
    REPR_PERMAN = 91
    GERENTE_UNI = 92
    DIRECTOR_TECNICO = 93
    MIEMBRO_JUNTA_RECTORA = 94
    SECRETARIO_JUNTA_RECTORA = 95
    PRESIDENTE_JUNTA_RECTORA = 96
    VICEPRESIDENTE_JUNTA_RECTORA = 97
    LIQUIDADOR_JUDICIAL = 98
    RLC_PER_S = 99  # Representante
    VICEPRESIDENTE_CONSEJO_RECTOR = 100
    COMITE_EJECUTIVO = 101
    AUDITOR_GRUPO = 102
    PRESIDENTE_COMISION_EJECUTIVA = 103
    VICEPRESIDENTE_COMISION_EJECUTIVA = 104
    VICEPRESIDENTE_PRIMERO = 105
    AUDITOR_SU_C_CON = 106
    MIEMBRO_CONSEJO_DIRECTIVO = 107
    PRESIDENTE_CONSEJO_DIRECTIVO = 108
    VICEPRESIDENTE_CONSEJO_DIRECTIVO = 109
    COMI_SIN_OBLI = 110  # ?
    CON_DEL_MANC = 111  # ?
    MIEMBRO_COMISION_NOM_RE = 112  # ?
    MIEMBRO_COMISION_DIRECCION = 113
    SECRETARIO_COMISION_DIRECTIVA = 114
    PRESIDENTE_COMISION_DIRECTIVA = 115
    SUPLENTE = 116
    COMISARIO_SI_O = 117  # ?
    COMISARIO_SUP_S = 118  # ?
    AUDITOR_MANCOMUNADO = 119
    MIEMBRO_COM_EIC = 120  # ?
    MIEMBRO_CTE_NYR = 121  # ?
    COM_NOMB = 122  # ?
    COM_ESTRATEG = 123  # ?
    APODERADO_CONJUNTO = 124

    _keywords = {'Presidente': PRESIDENTE,
                 'PRESIDENTE': PRESIDENTE,
                 'Vicepresid.': VICEPRESIDENTE,
                 'VICEPRESIDEN': VICEPRESIDENTE,
                 'Consejero': CONSEJERO,
                 'Consj.Domini': CONSEJERO_DOMINI,
                 'Secretario': SECRETARIO,
                 'SECRETARIO': SECRETARIO,
                 'Vicesecret.': VICESECRETARIO,
                 'VICESECRET.': VICESECRETARIO,
                 'Cons.Del.Man': CONSEJERO_DELEGADO_MANCOMUNADO,
                 'CONS.DEL.MAN': CONSEJERO_DELEGADO_MANCOMUNADO,
                 'Mie.Cons.Rec': MIEMBRO_CONSEJO_RECTOR,
                 'Miem.C.Ret': MIEMBRO_CONSEJO_RECTOR,
                 'Pre.Cons.Rec': PRESIDENTE_CONSEJO_RECTOR,
                 'Pr.C.Ret': PRESIDENTE_CONSEJO_RECTOR,
                 'Sec.Cons.Rec': SECRETARIO_CONSEJO_RECTOR,
                 'Sec.C.Ret': SECRETARIO_CONSEJO_RECTOR,
                 'Adm. Unico': ADM_UNICO,
                 'Adm. unico': ADM_UNICO,
                 'ADM.UNICO': ADM_UNICO,
                 'Admin.Unico': ADM_UNICO,
                 'Adm. Solid.': ADM_SOLID,
                 'ADM.SOLIDAR.': ADM_SOLID,
                 'Admin.Solid': ADM_SOLID,
                 'ADM.CONCURS.': ADM_CONCURS,
                 'Admin.Conc': ADM_CONCURS,
                 'Adm. Mancom': ADM_MANCOM,
                 'Admin.Manc': ADM_MANCOM,
                 'ADM.CONJUNTO': ADM_CONJUNTO,
                 'Apoderado': APODERADO,
                 'APODERADO': APODERADO,
                 'Apo.Man.Soli': APODERADO_MANCOMUNADO_SOLIDARIO,
                 'Apo.Manc.': APODERADO_MANCOMUNADO,
                 'APOD.MANCOMU': APODERADO_MANCOMUNADO,
                 'Adm. Mancom.': APODERADO_MANCOMUNADO,
                 'Apo.Sol.': APODERADO_SOLIDARIO,
                 'Apod.Solid': APODERADO_SOLIDARIO,
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
                 'Liquidador M': LIQUIDADOR_MANCOMUNADO,
                 'REPR.143 RRM': REPR_143_RRM,
                 'CONSEJERO': CONSEJERO,
                 'CONS.DEL.M/S': CONS_DEL_M_S,
                 'SecreNoConsj': SECRETARIO_NO_CONSEJ,
                 'SECR.NO CONS': SECRETARIO_NO_CONSEJ,
                 'Scr:no.Cons': SECRETARIO_NO_CONSEJ,
                 'VsecrNoConsj': VICESECRETARIO_NO_CONSJ,
                 'V-SEC NO CON': VICESECRETARIO_NO_CONSJ,
                 'Vcsec.no.Con': VICESECRETARIO_NO_CONSJ,
                 'Auditor': AUDITOR,
                 'Aud.C.Con.': AUDITOR_CUENTAS_CONSOLIDADAS,
                 'Aud.Supl.': AUDITOR_SUPL,
                 'Auditor Sup.': AUDITOR_SUPL,
                 'Ent.Reg.Cont': ENT_REG_CONT,
                 'EntidDeposit': ENTIDAD_DEPOSITARIA,
                 'ENT.DEPOSIT.': ENTIDAD_DEPOSITARIA,
                 'M.Comit.Aud': MIEMBRO_COMIT_AUD,
                 'Sec.Comit.Au': SECRETARIO_COMIT_AUD,
                 'Pte.Comit.Au': PRESIDENTE_COMIT_AUD,
                 'Pte. C. Aud.': PRESIDENTE_COMIT_AUD,
                 'Pres.Com.Ctr': PRESIDENTE_COMISION_CONTROL,
                 'Secr.Com.Ctr': SECRETARIO_COMISION_CONTROL,
                 'Miem.Com.Ctr': MIEMBRO_COMISION_CONTROL,
                 'MRO.COMS.CTR': MIEMBRO_COMISION_CONTROL,
                 'Miem.Com.Ej.': MIEMBRO_COMISION_EJECUTIVA,
                 'MRO.COMS.EJE': MIEMBRO_COMISION_EJECUTIVA,
                 'R.L.C.Perma.': RLC_PERMA,
                 'R.L.C.Per.M.': RLC_PERMA,
                 'R.L.C.Per.S.': RLC_PER_S,
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
                 'PRE.COMS.D.I': PRESIDENTE_COMS_D_I,
                 'Pte.Com.Inv': PRESIDENTE_COMS_D_I,
                 'M.Comit.Inv': MIEMBRO_COMITE_INV,
                 'S.N.C.C.D.I.': S_N_C_C_D_I,
                 'VS.N.C.C.D.I': VS_N_C_C_D_I,
                 'No definido': NO_DEFINIDO,
                 'L. Asesor': LETRADO_ASESOR,
                 'Exp.Ind.': EXP_IND,
                 'Mmbr.Com.Liq': MIEMBRO_COM_LIQ,
                 'Miem.Com.Liq': MIEMBRO_COM_LIQ,
                 'Pres.Com.Liq': PRESIDENTE_COM_LIQ,
                 'Secr.Com.Liq': SECRETARIO_COM_LIQ,
                 'Ger.Com.Ger': GER_COM_GER,
                 'ADMINISTR.': ADMINISTRADOR,
                 'Administrad': ADMINISTRADOR,
                 'VOCAL JTA.DI': VOCAL_JUNTA_DIRECTIVA,
                 'VOC.S.JTA.DI': VOCAL_SECUNDARIO_JUNTA_DIRECTIVA,
                 'V-PRE.JTA.DI': VICEPRESIDENTE_JUNTA_DIRECTIVA,
                 'V-PR.S.JTA.D': VICEPRESIDENTE_SEGUNDO_JUNTA_DIRECTIVA,
                 'TESOR.JTA.DI': TESORERO_JUNTA_DIRECTIVA,
                 'Director': DIRECTOR,
                 'Def.Particip': DEF_PARTICIP,
                 'Adm.Judicial': ADM_JUDICIAL,
                 'Adm.Supl.': ADM_SUPL,
                 'Apod.D.Gral.': APOD_D_GENERAL,
                 'Com. Audit.': COM_AUDIT,
                 'REPR.PERMAN.': REPR_PERMAN,
                 'Gerente Uni.': GERENTE_UNI,
                 'Dir. Técnico': DIRECTOR_TECNICO,
                 'Aud.Su.C.Con': AUDITOR_SU_C_CON,
                 'Miem.J.Rec': MIEMBRO_JUNTA_RECTORA,
                 'Pres.J.Rec': PRESIDENTE_JUNTA_RECTORA,
                 'Sec.J.Rec': SECRETARIO_JUNTA_RECTORA,
                 'Vic.Junt.Rec': VICEPRESIDENTE_JUNTA_RECTORA,
                 'Liq.Judicial': LIQUIDADOR_JUDICIAL,
                 'Miem.Con.Dir': MIEMBRO_CONSEJO_DIRECTIVO,
                 'Pres.Con.Dir': PRESIDENTE_CONSEJO_DIRECTIVO,
                 'Vpre.Con.Dir': VICEPRESIDENTE_CONSEJO_DIRECTIVO,
                 'ComiSinObli': COMI_SIN_OBLI,
                 'Con.Del.manc': CON_DEL_MANC,
                 'M.COM.NOM.RE': MIEMBRO_COMISION_NOM_RE,
                 'Pres.Com.Ej.': PRESIDENTE_COMISION_EJECUTIVA,
                 'Pr.Com.Ejecu': PRESIDENTE_COMISION_EJECUTIVA,
                 'Vpr.Com.Ejec': VICEPRESIDENTE_COMISION_EJECUTIVA,
                 'Vicpres C.E': VICEPRESIDENTE_COMISION_EJECUTIVA,
                 'Com.Ejecutiv': COMITE_EJECUTIVO,
                 'COM.EJECUTIV': COMITE_EJECUTIVO,
                 'Vicepresi.1º': VICEPRESIDENTE_PRIMERO,
                 'Vcp.Cons.Rec': VICEPRESIDENTE_CONSEJO_RECTOR,
                 'Auditor Grup': AUDITOR_GRUPO,
                 'MiemComDire': MIEMBRO_COMISION_DIRECCION,
                 'SecrComDirec': SECRETARIO_COMISION_DIRECTIVA,
                 'PresComDirec': PRESIDENTE_COMISION_DIRECTIVA,
                 'Suplente': SUPLENTE,
                 'COMISAR.SI.O': COMISARIO_SI_O,
                 'COMISR.SUP.S': COMISARIO_SUP_S,
                 'Aud.Manc': AUDITOR_MANCOMUNADO,
                 'Miem.COM.EIC': MIEMBRO_COM_EIC,
                 'Mbro.Cte.NyR': MIEMBRO_CTE_NYR,
                 'Com.Nomb.': COM_NOMB,
                 'Com estrateg': COM_ESTRATEG,
                 'APOD.CONJUN.': APODERADO_CONJUNTO,

                 # hack
                 'Sociedades beneficiarias': SOCIEDADES_BENEFICIARIAS,
                 'Sociedades fusionadas': SOCIEDADES_FUSIONADAS,
                 }
    KEYWORDS = list(six.viewkeys(_keywords))

    @staticmethod
    def from_string(string):
        return CARGO._keywords[string]
