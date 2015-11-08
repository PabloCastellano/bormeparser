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
    ADMINISTRADOR_UNICO = 7
    MIEMBRO_CONSEJO_RECTOR = 8
    PRESIDENTE_CONSEJO_RECTOR = 9
    SECRETARIO_CONSEJO_RECTOR = 10
    ADMINISTRADOR_SOLIDARIO = 11
    APODERADO = 12
    SOCIO_PROFESIONAL = 13
    APODERADO_MANCOMUNADO_SOLIDARIO = 14
    APODERADO_MANCOMUNADO = 15
    APODERADO_SOLIDARIO = 16
    ADM_MANCOM = 17
    CONSEJERO_DELEGADO_MANCOMUNADO_SOLIDARIO = 18
    CONS_DEL_SOL = 19
    REPRESENTANTE = 20
    CONS_DELEGADO = 21
    APODERADO_SOLIDARIO_MANCOMUNADO = 22
    LIQUISOLI = 23
    LIQUIDADOR = 24
    APODERADO_SOL = 25
    REPR_143_RRM = 26
    AUDITOR_CUENTAS_CONSOLIDADAS = 27
    SECRETARIO_NO_CONSEJERO = 28
    CONS_DEL_M_S = 29
    VICESECRETARIO_NO_CONSEJERO = 30
    AUDITOR = 31
    ADM_CONCURS = 32
    REP_ADM_CONC = 33
    AUDITOR_SUPLENTE = 34
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
    SECRETARIO_JGPV = 48
    MIEMBRO_JGPV = 49
    PRESIDENTE_JGPV = 50
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
    ADM_SUPLENTE = 86
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
    MIEMBRO_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES = 121  # NyR
    COM_NOMB = 122  # ?
    COM_ESTRATEG = 123  # ?
    APODERADO_CONJUNTO = 124
    R_C_P_SOLMAN = 125
    VOCAL_5 = 126
    VOCAL_6 = 127
    VOCAL_7 = 128
    REPRESENTANTE_SUCURS = 129
    SUB_GENERAL = 130
    MED_CONCUSAL = 131
    LIQUIDADOR_CONC = 132
    DIRECTOR_GENERAL_SUPLENTE = 133
    CON_IND = 134
    ADMINISTRADOR_MANCOMUNADO = 135
    PRESIDENTE_JUNTA_DIRECTIVA = 136
    DIRECTOR_SUCURSAL = 137
    MIEMBRO_COMISION_SEQ = 138
    TESORERO_CONSEJO_RECTOR = 139
    TESORERO_COMISION_EJECUTIVA_C = 140
    MIEMBRO_COMISION_EJECUTIVA_CR = 141
    PRESIDENTE_COMISION_A_YC = 142
    PROMOTOR = 143
    DEPOSITARIO = 144
    VOCAL_COMIT_AUD = 145
    DIRECTOR_FABRICA = 146
    C_CTR_E_PROM = 147
    INTERVENTOR = 148
    INTERVENTOR_JUDICIAL = 149
    ADMINISTRADOR_SOLIDARIO_SUPLENTE = 150
    AUDITOR_SUPLENTE_CUENTAS_CONSOLIDADAS = 151
    ENTIDAD_COGESTORA = 152
    VICEPRESIDENTE_JGPV = 153
    PRESIDENTE_COMITE_INV = 154
    VICEPRESIDENTE_COMITE_INV = 155
    SECRETARIO_COMITE_INV = 156
    VICESECRETARIO_COMITE_INV = 157
    SECRETARIO_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES = 158
    DIRECTOR_GENERAL_ADJUNTO = 159
    PRESIDENTE_COMISION_DELEGADA = 160
    SECRETARIO_COMISION_DELEGADA = 161
    MIEMBRO_COMISION_DELEGADA = 162
    AUDITOR_TIT_GRUP = 163
    AUDITOR_CONJUNTO = 164
    AUDITOR_CUENTAS_CONSOLIDADAS_CONJUNTO = 165
    MIEMBRO_COMISION_REC = 166
    SECRETARIO_COMISION_REC = 167
    DELEGADO = 168
    VOCAL_E_P_JUNTA_DIRECTIVA = 169
    PRESIDENTE_COMISION_AYR = 170
    MIEMBRO_COMISION_AYR = 171
    SEC_CM_DIR_N_CON = 172
    CONSEJO_RECTOR = 173
    SECRETARIO_COMISION_O_S = 174
    MIEMBRO_COMISION_O_S = 175
    VICEPRESIDENTE_COMISION_O_S = 176
    VICESECRETARIO_COMISION_O_S = 177
    PRESIDENTE_COMISION_O_S = 178
    CONSEJERO_SUPLENTE = 179
    S_NO_MI_CO_E = 180
    SOCIO_GESTOR = 181
    VICESECRETARIO_C_E = 182
    SECRETARIO_COMISION_OP_VIN = 183
    SECRETARIO_COMISION_AU_CNT = 184
    MIEMBRO_COMISION_RI = 185
    ADMINISTRADOR_PROV_SOLIDARIO = 186
    CONSEJERO_INTERIN = 187
    ADJ_GERENCIA = 188
    PRESIDENTE_HONORIFICO = 189
    PRESIDENTE_COMITE_ADM_RES = 190
    REPRESENTANTE_FISCAL = 191
    PRESIDENTE_EJECUTIVO = 192
    ADMINISTRADOR_MANCOMUNADO_SUPLENTE = 193
    VICESECRETARIO_COMISION_CONTROL = 194
    DIRECTOR_ADMINISTRACION = 195
    SUBDIRECTOR_GENERAL = 196
    MIEMBRO_COM_GER = 197
    ADMINISTRADOR_ADJUNTO = 198
    VICESECRETARIO_JUNTA_DIRECTIVA = 199
    COM_AUDIT_CTRL = 200
    MIEMBRO_COM_AUD = 201
    SECRETARIO_COMISION_EJECUTIVA = 202
    SECRETARIO_COMISION_EJECUTIVA_NO_CONSEJERO = 203
    PRESIDENTE_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES = 204
    MIEMBRO_COMISION_AU_CNT = 205
    SINDICO = 206
    VOCAL_8_CON_REC = 207
    SUPLENTE_CONSEJO_RECTOR = 208
    D_G_CONSEJO_RECTOR = 209
    SECRETARIO_NO_CONSEJERO_GO = 210
    MIEMBRO_CONSEJERO_GO = 211
    VICEPRESIDENTE_COMISION_CONTROL = 212
    SUPLENTE_COMISION_CONTROL = 213
    MIEMBRO_AGPV = 214
    VOCAL_3_JUNTA_DIRECTIVA = 215
    VOCAL_4_JUNTA_DIRECTIVA = 216
    VOCAL_10_CON_REC = 217
    MIEMBRO_COM_CTO = 218
    VICEPRESIDENTE_PRIMERO_COM_CTO = 219
    VICEPRESIDENTE_SEGUNDO_COM_CTO = 220
    VICESECRETARIO_PRIMERO_COM_CTO = 221
    VICESECRETARIO_SEGUNDO_COM_CTO = 222
    COMISION_ACREED = 223
    SUPLENTE_COMISION_ACREED = 224
    PRESIDENTE_COM_EIC = 225
    COPRESIDENTE = 226
    VICESECRETARIO_CONSEJO_RECTOR = 227
    SOCIO_COLECTIVO = 228
    DIRECTOR_COMERCIAL = 229
    SECRETARIO_COMISION_EJECUTIVA_CR = 230
    PRESIDENTE_J_ADM = 231
    VICEPRESIDENTE_J_ADM = 232
    SECRETARIO_J_ADM = 233
    TESORERO_J_ADM = 234
    CONTADOR = 235
    PRESIDENTE_COMISION_DIRECCION = 236
    PRESIDENTE_COMISION_AU_CNT = 237
    MIEMBRO_COMISION_AU_CUM = 238
    SE_TEC_NO_CO = 239
    MIEMBRO_S_O_CTR = 240
    PRESIDENTE_COM_AUD = 241
    OTROS = 242
    LIQUIDADOR_SUPLENTE = 243
    CONSEJERO_HONORA = 244
    DIRECTOR_GENERAL_ADM = 245
    GERENTE_EJECUTIVO = 246
    ADMINISTRADOR_PROV_SOLIDARIO_EF = 247
    MIEMBRO_COMITE_CON = 248
    PRESIDENTE_COMITE_PRO = 249
    VICEPRESIDENTE_COMITE_PRO = 250
    SECRETARIO_COMITE_PRO = 251
    MIEMBRO_COMITE_PRO = 252
    SECRETARIO_GENERAL = 253
    DIRECTOR_EJECUTIVO = 254
    SOCIO_UNICO_PROFESIONAL = 255
    VICEPRESIDENTE_SEGUNDO = 256
    SECRETARIO_GENERAL_ADJUNTO = 257
    VICESECRETARIO_NO_CONSEJERO_SEGUNDO = 258
    MIEMBRO_COMISION_RETR = 259
    ADMINISTRADOR_PRIMERO = 260
    REPRESENTANTE_PLAN = 261
    REPRESENTANTE_SUPLENTE = 262
    CONSEJERO_INDEPENDIENTE = 263
    DEPOSITARIO_COMISION_CONTROL = 264
    ENTIDAD_GESTORA_ACT = 265
    ENTIDAD_GESTORA_INDEPENDIENTE = 266
    DIRECTOR_DEPARTAMENTO = 267
    DIRECTOR_EXPLOTA = 268
    DIRECTOR_FINANCIERO = 269
    SUBDIRECTOR = 270
    SECRETARIO_NO_CONSEJERO_COMISION_EJECUTIVA = 271
    INTERVENTOR_SOLIDARIO = 272
    VOCAL_SUPLENTE = 273
    VICEPRESIDENTE_HONORIFICO = 274
    VICEPRESIDENTE_COMISION_DIRECTIVA = 275
    MIEMBRO_COMISION_CYA = 276
    MIEMBRO_COMISION_VIG = 277
    SUPLENTE_COMISION_VIG = 278
    AG_REV_TIT = 279
    PRESIDENTE_COMISION_RIESGOS = 280
    VICEPRESIDENTE_COMISION_RIESGOS = 281
    CONSEJERO_COMISION_RIESGOS = 282
    COMS_VIGILAN = 283
    MIEMBRO_COMISION_ACR = 284
    FUNDADOR = 285
    GERENTE_SMCP = 286
    SUPLENTE_COMISION_CT = 287
    MIEMBRO_CDCA = 288
    OTORGANTE = 289
    SUPLENTE_COMISION_LI = 290
    PRESEN_CONC = 291
    PRESIDENTE_COMISION_SEG = 292
    MIEMBRO_COMISION_SEG = 293
    AUX_ADMINISTRADOR_CONC = 294
    MIEMBRO_C_COMISION_PERM = 295
    MANDATARIO = 296
    CONSEJERO_COMISION_DELEGADA = 297
    ADMINISTRADOR_PROV = 298
    SECRETARIO_COMISION_AYR = 299
    DELEGADO_GENERAL = 300

    _keywords = {'Presidente': PRESIDENTE,
                 'PRESIDENTE': PRESIDENTE,
                 'Pdte.': PRESIDENTE,
                 'PresEjecutiv': PRESIDENTE_EJECUTIVO,
                 'PRES.EJECUT.': PRESIDENTE_EJECUTIVO,
                 'COPRESIDENTE': COPRESIDENTE,
                 'Vicepresid.': VICEPRESIDENTE,
                 'VICEPRESIDEN': VICEPRESIDENTE,
                 'Vicepresiden': VICEPRESIDENTE,
                 'VICEPRESID.2': VICEPRESIDENTE_SEGUNDO,
                 'Consejero': CONSEJERO,
                 'Consj.Domini': CONSEJERO_DOMINI,
                 'Secretario': SECRETARIO,
                 'SECRETARIO': SECRETARIO,
                 'Secret.Gral.': SECRETARIO_GENERAL,
                 'Secr.Gral.Ad': SECRETARIO_GENERAL_ADJUNTO,
                 'Vicesecret.': VICESECRETARIO,
                 'VICESECRET.': VICESECRETARIO,
                 'VsecrNoConsj': VICESECRETARIO_NO_CONSEJERO,
                 'V-SEC NO CON': VICESECRETARIO_NO_CONSEJERO,
                 'Vcsec.no.Con': VICESECRETARIO_NO_CONSEJERO,
                 'V- SEC NO CON': VICESECRETARIO_NO_CONSEJERO,
                 'V-SEC.NO.C.2': VICESECRETARIO_NO_CONSEJERO_SEGUNDO,
                 'Cons.Del.Man': CONSEJERO_DELEGADO_MANCOMUNADO,
                 'CONS.DEL.MAN': CONSEJERO_DELEGADO_MANCOMUNADO,
                 'Vcs.Cons.Rec': VICESECRETARIO_CONSEJO_RECTOR,
                 'Mie.Cons.Rec': MIEMBRO_CONSEJO_RECTOR,
                 'Miem.Co.Rec': MIEMBRO_CONSEJO_RECTOR,
                 'Miem.C.Ret': MIEMBRO_CONSEJO_RECTOR,
                 'M.Com.Retr.': MIEMBRO_COMISION_RETR,
                 'Pre.Cons.Rec': PRESIDENTE_CONSEJO_RECTOR,
                 'PRES.CON.REC': PRESIDENTE_CONSEJO_RECTOR,
                 'Pr.C.Ret': PRESIDENTE_CONSEJO_RECTOR,
                 'Pres.Com.Ret': PRESIDENTE_CONSEJO_RECTOR,
                 'Sec.Cons.Rec': SECRETARIO_CONSEJO_RECTOR,
                 'SECR.CON.REC': SECRETARIO_CONSEJO_RECTOR,
                 'Sec.C.Ret': SECRETARIO_CONSEJO_RECTOR,
                 'Secr.C.Ret': SECRETARIO_CONSEJO_RECTOR,
                 'SUPL2.CON.RE': SUPLENTE_CONSEJO_RECTOR,
                 'Vcp.Cons.Rec': VICEPRESIDENTE_CONSEJO_RECTOR,
                 'Tes.C.Rec': TESORERO_CONSEJO_RECTOR,
                 'CONS.RECTOR': CONSEJO_RECTOR,
                 'D.G.Cons.Rec': D_G_CONSEJO_RECTOR,
                 'Adm. Unico': ADMINISTRADOR_UNICO,
                 'Adm. Unico.': ADMINISTRADOR_UNICO,
                 'Adm. unico': ADMINISTRADOR_UNICO,
                 'ADM.UNICO': ADMINISTRADOR_UNICO,
                 'Admin.Unico': ADMINISTRADOR_UNICO,
                 'DM.UNICO 2': ADMINISTRADOR_UNICO,
                 'Adm. Solid.': ADMINISTRADOR_SOLIDARIO,
                 'ADM.SOLIDAR.': ADMINISTRADOR_SOLIDARIO,
                 'Admin.Solid': ADMINISTRADOR_SOLIDARIO,
                 'ADM.CONCURS.': ADM_CONCURS,
                 'Adm.Concur': ADM_CONCURS,
                 'Admin.Conc': ADM_CONCURS,
                 'Adm. Mancom': ADM_MANCOM,
                 'Admin.Manc': ADM_MANCOM,
                 'ADM.CONJUNTO': ADM_CONJUNTO,
                 'Adm. Mancom.': ADMINISTRADOR_MANCOMUNADO,
                 'Adm. Manco.': ADMINISTRADOR_MANCOMUNADO,
                 'Adm.Man.Supl': ADMINISTRADOR_MANCOMUNADO_SUPLENTE,
                 'ADM.SUP.MAN.': ADMINISTRADOR_MANCOMUNADO_SUPLENTE,
                 'Admin.1º': ADMINISTRADOR_PRIMERO,
                 'Apoderado': APODERADO,
                 'APODERADO': APODERADO,
                 'poderado 1': APODERADO,
                 'Apo.Man.Soli': APODERADO_MANCOMUNADO_SOLIDARIO,
                 'Apo.Manc.': APODERADO_MANCOMUNADO,
                 'Apod.Manc': APODERADO_MANCOMUNADO,
                 'APOD.MANCOMU': APODERADO_MANCOMUNADO,
                 'Apo.Sol.': APODERADO_SOLIDARIO,
                 'Apod.Solid': APODERADO_SOLIDARIO,
                 'APODERAD.SOL': APODERADO_SOL,
                 'APOD.CONJUN.': APODERADO_CONJUNTO,
                 'Apo.D.Gral.': APODERADO_D_GENERAL,
                 'APOD.SOL/MAN': APODERADO_SOLIDARIO_MANCOMUNADO,
                 'Apod.Sol-man': APODERADO_SOLIDARIO_MANCOMUNADO,
                 'Soc.Prof.': SOCIO_PROFESIONAL,
                 'Soc.Uni.Prof': SOCIO_UNICO_PROFESIONAL,
                 'Co.De.Ma.So': CONSEJERO_DELEGADO_MANCOMUNADO_SOLIDARIO,
                 'Cons.Del.Sol': CONS_DEL_SOL,
                 'Representan': REPRESENTANTE,
                 'Represent.': REPRESENTANTE,
                 'REPRESENT.': REPRESENTANTE,
                 'REPRESENTAN.': REPRESENTANTE,
                 'REPR.SUCURS.': REPRESENTANTE_SUCURS,
                 'Rpte. Suc.': REPRESENTANTE_SUCURS,
                 'Rep.SUC.': REPRESENTANTE_SUCURS,
                 'REPRE.FISCAL': REPRESENTANTE_FISCAL,
                 'Repre.Fiscal': REPRESENTANTE_FISCAL,
                 'Repres.Plan.': REPRESENTANTE_PLAN,
                 'RepresSuplen': REPRESENTANTE_SUPLENTE,
                 'Con.Delegado': CONS_DELEGADO,
                 'CONS. DELEG.': CONS_DELEGADO,
                 'Cons.Delegad': CONS_DELEGADO,
                 'Liquidador': LIQUIDADOR,
                 'LIQUIDADOR': LIQUIDADOR,
                 'Liq.Sup.': LIQUIDADOR_SUPLENTE,
                 'LiquiSoli': LIQUISOLI,
                 'LiqSolid': LIQUISOLI,
                 'Liquidador M': LIQUIDADOR_MANCOMUNADO,
                 'LiqManc': LIQUIDADOR_MANCOMUNADO,
                 'LIQUID.MANC.': LIQUIDADOR_MANCOMUNADO,
                 'Liquid.manc': LIQUIDADOR_MANCOMUNADO,
                 'LIQ.CONC.': LIQUIDADOR_CONC,
                 'Liquid.conc.': LIQUIDADOR_CONC,
                 'LiqC': LIQUIDADOR_CONC,
                 'LiqUnico': LIQUIDADOR_UNICO,
                 'Liq.Judicial': LIQUIDADOR_JUDICIAL,
                 'REPR.143 RRM': REPR_143_RRM,
                 'CONSEJERO': CONSEJERO,
                 'ConsejSuplen': CONSEJERO_SUPLENTE,
                 'Consj. Supl.': CONSEJERO_SUPLENTE,
                 'CONS.SUPLENT': CONSEJERO_SUPLENTE,
                 'Cons.Interin': CONSEJERO_INTERIN,
                 'CONS.HONORA.': CONSEJERO_HONORA,
                 'Cons. Idpte.': CONSEJERO_INDEPENDIENTE,
                 'CONS.DEL.M/S': CONS_DEL_M_S,
                 'SecreNoConsj': SECRETARIO_NO_CONSEJERO,
                 'SECR.NO CONS': SECRETARIO_NO_CONSEJERO,
                 'Scr:no.Cons': SECRETARIO_NO_CONSEJERO,
                 'S.NO CONS.GO': SECRETARIO_NO_CONSEJERO_GO,
                 'MBRO.CONS.GO': MIEMBRO_CONSEJERO_GO,
                 'Auditor': AUDITOR,
                 'Aud.C.Con.': AUDITOR_CUENTAS_CONSOLIDADAS,
                 'AUDT.CTS.CON': AUDITOR_CUENTAS_CONSOLIDADAS,
                 'Aud.Supl.': AUDITOR_SUPLENTE,
                 'Auditor Sup.': AUDITOR_SUPLENTE,
                 'AUDITOR SUP.': AUDITOR_SUPLENTE,
                 'Aud.Supl.CC': AUDITOR_SUPLENTE_CUENTAS_CONSOLIDADAS,
                 'Aud.Supl.C.C': AUDITOR_SUPLENTE_CUENTAS_CONSOLIDADAS,
                 'Ent.Reg.Cont': ENT_REG_CONT,
                 'EntidDeposit': ENTIDAD_DEPOSITARIA,
                 'ENT.DEPOSIT.': ENTIDAD_DEPOSITARIA,
                 'Ent.Deposita': ENTIDAD_DEPOSITARIA,
                 'M.Comit.Aud': MIEMBRO_COMIT_AUD,
                 'Sec.Comit.Au': SECRETARIO_COMIT_AUD,
                 'SecComAudit.': SECRETARIO_COMIT_AUD,
                 'Pte.Comit.Au': PRESIDENTE_COMIT_AUD,
                 'Pte. C. Aud.': PRESIDENTE_COMIT_AUD,
                 'PreComAudit.': PRESIDENTE_COMIT_AUD,
                 'PreComAudit': PRESIDENTE_COMIT_AUD,
                 'VocComAudit.': VOCAL_COMIT_AUD,
                 'VocComAudit': VOCAL_COMIT_AUD,
                 'Pres.Com.Ctr': PRESIDENTE_COMISION_CONTROL,
                 'PRE.COMS.CTR': PRESIDENTE_COMISION_CONTROL,
                 'PRES.COM.CON': PRESIDENTE_COMISION_CONTROL,
                 'Vpr.Com.Ctr': VICEPRESIDENTE_COMISION_CONTROL,
                 'V-PRE.COMS.C': VICEPRESIDENTE_COMISION_CONTROL,
                 'Secr.Com.Ctr': SECRETARIO_COMISION_CONTROL,
                 'SEC.COMS.CTR': SECRETARIO_COMISION_CONTROL,
                 'Vices.Com.Ct': VICESECRETARIO_COMISION_CONTROL,
                 'Miem.Com.Ctr': MIEMBRO_COMISION_CONTROL,
                 'MRO.COMS.CTR': MIEMBRO_COMISION_CONTROL,
                 'MBRO.COM.CRT': MIEMBRO_COMISION_CONTROL,
                 'Supl.Comi.C.': SUPLENTE_COMISION_CONTROL,
                 'Dep.Com.Ctr.': DEPOSITARIO_COMISION_CONTROL,
                 'R.L.C.Perma.': RLC_PERMA,
                 'R.L.C.Perm.': RLC_PERMA,
                 'R.L.C.Per.M.': RLC_PERMA,
                 'R.L.C.Per.S.': RLC_PER_S,
                 'Sec.J.G.P.V': SECRETARIO_JGPV,
                 'Miem.J.G.P.V': MIEMBRO_JGPV,
                 'Pres.J.G.P.V': PRESIDENTE_JGPV,
                 'Vpre.J.G.P.V': VICEPRESIDENTE_JGPV,
                 'Miem.A.G.P.V': MIEMBRO_AGPV,
                 'Tesorero': TESORERO,
                 'TESORERO': TESORERO,
                 'REP.ADM.CONC': REP_ADM_CONC,
                 'Comisario': COMISARIO,
                 'COMISARIO': COMISARIO,
                 'Comis.Contro': COMISARIO,
                 'Gerente': GERENTE,
                 'GERENTE': GERENTE,
                 'Cons.Del.C.R': CONS_DEL_C_R,
                 'Ent. Gestora': ENTIDAD_GESTORA,
                 'Ent.Gestora': ENTIDAD_GESTORA,
                 'ENTI.GESTORA': ENTIDAD_GESTORA,
                 'Ent.Gest.Act': ENTIDAD_GESTORA_ACT,
                 'ENT.GEST.IND': ENTIDAD_GESTORA_INDEPENDIENTE,
                 'ENT.COGESTOR': ENTIDAD_COGESTORA,
                 'Auditor Titu': AUDITOR_TITU,
                 'AUDIT.CUENT.': AUDITOR_CUENTAS,
                 'Director': DIRECTOR,
                 'DIRECTOR': DIRECTOR,
                 'Dir.Adm.': DIRECTOR_ADMINISTRACION,
                 'DTOR.ADMINIS': DIRECTOR_ADMINISTRACION,
                 'DTOR.DEPART.': DIRECTOR_DEPARTAMENTO,
                 'DTOR.COMERC.': DIRECTOR_COMERCIAL,
                 'Dir. General': DIRECTOR_GENERAL,
                 'Dir.Gral.': DIRECTOR_GENERAL,
                 'DTOR.GENERAL': DIRECTOR_GENERAL,
                 'Dtor.General': DIRECTOR_GENERAL,
                 'DIRECTOR GEN': DIRECTOR_GENERAL,
                 'DTOR.GEN.ADM': DIRECTOR_GENERAL_ADM,
                 'DTOR.GEN.ADJ': DIRECTOR_GENERAL_ADJUNTO,
                 'Dir.Gral.Adj': DIRECTOR_GENERAL_ADJUNTO,
                 'DTOR.EJECUT.': DIRECTOR_EJECUTIVO,
                 'DTOR.EXPLOTA': DIRECTOR_EXPLOTA,
                 'DTOR.FABRICA': DIRECTOR_FABRICA,
                 'DTOR.FINANC.': DIRECTOR_FINANCIERO,
                 'DTOR.SUCURS.': DIRECTOR_SUCURSAL,
                 'DTOR.TECNICO': DIRECTOR_TECNICO,
                 'Dir. Técnico': DIRECTOR_TECNICO,
                 'D. Comercial': DIRECTOR_COMERCIAL,
                 'Dir.Gen.Spl': DIRECTOR_GENERAL_SUPLENTE,
                 'Subdirec': SUBDIRECTOR,
                 'SUBDTOR.GNRL': SUBDIRECTOR_GENERAL,
                 'Subdir.Gral.': SUBDIRECTOR_GENERAL,
                 'Socio': SOCIO,
                 'Socio único': SOCIO_UNICO,
                 'SOCIO COLECT': SOCIO_COLECTIVO,
                 'SocGestor': SOCIO_GESTOR,
                 'COMS.DEL.INV': COMS_DEL_INV,
                 'PRE.COMS.D.I': PRESIDENTE_COMS_D_I,
                 'Pte.Com.Inv': PRESIDENTE_COMS_D_I,
                 'M.Comit.Inv': MIEMBRO_COMITE_INV,
                 'MBRO.COM.INV': MIEMBRO_COMITE_INV,
                 'M.Com.Inv': MIEMBRO_COMITE_INV,
                 'PRES.COM.INV': PRESIDENTE_COMITE_INV,
                 'V-PRE.COM.IN': VICEPRESIDENTE_COMITE_INV,
                 'V- PRE.COM.IN': VICEPRESIDENTE_COMITE_INV,
                 'SECR.COM.INV': SECRETARIO_COMITE_INV,
                 'V-SEC.COM.IN': VICESECRETARIO_COMITE_INV,
                 'S.N.C.C.D.I.': S_N_C_C_D_I,
                 'VS.N.C.C.D.I': VS_N_C_C_D_I,
                 'No definido': NO_DEFINIDO,
                 'L. Asesor': LETRADO_ASESOR,
                 'LETRAD.ASES.': LETRADO_ASESOR,
                 'LETRD.ASESOR': LETRADO_ASESOR,
                 'Exp.Ind.': EXP_IND,
                 'Mmbr.Com.Liq': MIEMBRO_COM_LIQ,
                 'MRO.COMS.LIQ': MIEMBRO_COM_LIQ,
                 'Miem.Com.Liq': MIEMBRO_COM_LIQ,
                 'M.Cons.Liq': MIEMBRO_COM_LIQ,
                 'Pres.Com.Liq': PRESIDENTE_COM_LIQ,
                 'Pr.Cons.Liq': PRESIDENTE_COM_LIQ,
                 'Secr.Com.Liq': SECRETARIO_COM_LIQ,
                 'Secr.Cons.Li': SECRETARIO_COM_LIQ,
                 'Ger.Com.Ger': GER_COM_GER,
                 'Miem.Com.Ger': MIEMBRO_COM_GER,
                 'MBRO.COM.GER': MIEMBRO_COM_GER,
                 'ADMINISTR.': ADMINISTRADOR,
                 'Administrad': ADMINISTRADOR,
                 'ADM.ADJUNTO': ADMINISTRADOR_ADJUNTO,
                 'PRESI.JTA.DI': PRESIDENTE_JUNTA_DIRECTIVA,
                 'Pres.J.Dir.': PRESIDENTE_JUNTA_DIRECTIVA,
                 'PRESID.JUNTA': PRESIDENTE_JUNTA_DIRECTIVA,
                 'V-PRE.JTA.DI': VICEPRESIDENTE_JUNTA_DIRECTIVA,
                 'Vpte.J.Dir.': VICEPRESIDENTE_JUNTA_DIRECTIVA,
                 'V-PR.S.JTA.D': VICEPRESIDENTE_SEGUNDO_JUNTA_DIRECTIVA,
                 'Vsec.J.Dir.': VICESECRETARIO_JUNTA_DIRECTIVA,
                 'Scrt.J.Dir.': SECRETARIO_JUNTA_DIRECTIVA,
                 'SEC.JTA.DIRE': SECRETARIO_JUNTA_DIRECTIVA,
                 'Miem.J.Dir.': MIEMBRO_JUNTA_DIRECTIVA,
                 'MBRO.JTA.DIR': MIEMBRO_JUNTA_DIRECTIVA,
                 'VOCAL JTA.DI': VOCAL_JUNTA_DIRECTIVA,
                 'VOC.S.JTA.DI': VOCAL_SECUNDARIO_JUNTA_DIRECTIVA,
                 'TESOR.JTA.DI': TESORERO_JUNTA_DIRECTIVA,
                 'VO.E.P.JT.DI': VOCAL_E_P_JUNTA_DIRECTIVA,
                 'VOC3.JTA.DIR': VOCAL_3_JUNTA_DIRECTIVA,
                 'VOC4.JTA.DIR': VOCAL_4_JUNTA_DIRECTIVA,
                 'Def.Particip': DEF_PARTICIP,
                 'DEF PARTICIP': DEF_PARTICIP,
                 'Defens.part.': DEF_PARTICIP,
                 'Def.part.': DEF_PARTICIP,
                 'Adm.Judicial': ADM_JUDICIAL,
                 'ADM.JUDICIAL': ADM_JUDICIAL,
                 'Admin.Judic': ADM_JUDICIAL,
                 'Adm.Supl.': ADM_SUPLENTE,
                 'ADM.SUPLENTE': ADM_SUPLENTE,
                 'Apod.D.Gral.': APOD_D_GENERAL,
                 'Com. Audit.': COM_AUDIT,
                 'COMIS.AUDITO': COM_AUDIT,
                 'COM.AUD.CTRL': COM_AUDIT_CTRL,
                 'PRE.COM.AUD.': PRESIDENTE_COM_AUD,
                 'MBRO.COM.AUD': MIEMBRO_COM_AUD,
                 'REPR.PERMAN.': REPR_PERMAN,
                 'Repr.perman': REPR_PERMAN,
                 'Gerente Uni.': GERENTE_UNI,
                 'Ger.Eje.': GERENTE_EJECUTIVO,
                 'Aud.Su.C.Con': AUDITOR_SU_C_CON,
                 'Miem.J.Rec': MIEMBRO_JUNTA_RECTORA,
                 'Pres.J.Rec': PRESIDENTE_JUNTA_RECTORA,
                 'PRE.JTA.RECT': PRESIDENTE_JUNTA_RECTORA,
                 'Sec.J.Rec': SECRETARIO_JUNTA_RECTORA,
                 'SEC.JTA.RECT': SECRETARIO_JUNTA_RECTORA,
                 'Vic.Junt.Rec': VICEPRESIDENTE_JUNTA_RECTORA,
                 'Miem.Con.Dir': MIEMBRO_CONSEJO_DIRECTIVO,
                 'Pres.Con.Dir': PRESIDENTE_CONSEJO_DIRECTIVO,
                 'Vpre.Con.Dir': VICEPRESIDENTE_CONSEJO_DIRECTIVO,
                 'ComiSinObli': COMI_SIN_OBLI,
                 'Con.Del.manc': CON_DEL_MANC,
                 'M.COM.NOM.RE': MIEMBRO_COMISION_NOM_RE,
                 'Pres.Com.Ej.': PRESIDENTE_COMISION_EJECUTIVA,
                 'PRES.COM.EJE': PRESIDENTE_COMISION_EJECUTIVA,
                 'PRE.COMS.EJE': PRESIDENTE_COMISION_EJECUTIVA,
                 'Pr.Com.Ejecu': PRESIDENTE_COMISION_EJECUTIVA,
                 'Pte.C.Ej': PRESIDENTE_COMISION_EJECUTIVA,
                 'P.Com.Ejec.': PRESIDENTE_COMISION_EJECUTIVA,
                 'Sec.Com.Ej.': SECRETARIO_COMISION_EJECUTIVA,
                 'Sec.C.Ej': SECRETARIO_COMISION_EJECUTIVA,
                 'S.NO.C.CO.EJ': SECRETARIO_NO_CONSEJERO_COMISION_EJECUTIVA,
                 'SecrCENoCon': SECRETARIO_COMISION_EJECUTIVA_NO_CONSEJERO,
                 'Vpr.Com.Ejec': VICEPRESIDENTE_COMISION_EJECUTIVA,
                 'Vicpres C.E': VICEPRESIDENTE_COMISION_EJECUTIVA,
                 'Miem.Com.Ej.': MIEMBRO_COMISION_EJECUTIVA,
                 'MRO.COMS.EJE': MIEMBRO_COMISION_EJECUTIVA,
                 'MBRO.COM.EJE': MIEMBRO_COMISION_EJECUTIVA,
                 'M.Com.Ej': MIEMBRO_COMISION_EJECUTIVA,
                 'Com.Ejecutiv': COMITE_EJECUTIVO,
                 'COM.EJECUTIV': COMITE_EJECUTIVO,
                 'Vicepresi.1º': VICEPRESIDENTE_PRIMERO,
                 'VICEPRESID.1': VICEPRESIDENTE_PRIMERO,
                 'Auditor Grup': AUDITOR_GRUPO,
                 'PRES.CON.DIR': PRESIDENTE_COMISION_DIRECCION,
                 'MiemComDire': MIEMBRO_COMISION_DIRECCION,
                 'MiemComDirec': MIEMBRO_COMISION_DIRECCION,
                 'MBRO.CON.DIR': MIEMBRO_COMISION_DIRECCION,
                 'MBRO.COM.DIR': MIEMBRO_COMISION_DIRECCION,
                 'MRO.COMS.DIR': MIEMBRO_COMISION_DIRECCION,
                 'SecrComDirec': SECRETARIO_COMISION_DIRECTIVA,
                 'PresComDirec': PRESIDENTE_COMISION_DIRECTIVA,
                 'Vte.Com.Dir.': VICEPRESIDENTE_COMISION_DIRECTIVA,
                 'Suplente': SUPLENTE,
                 'COMISAR.SI.O': COMISARIO_SI_O,
                 'COMISR.SUP.S': COMISARIO_SUP_S,
                 'Aud.Manc': AUDITOR_MANCOMUNADO,
                 'Miem.COM.EIC': MIEMBRO_COM_EIC,
                 'Pres.COM.EIC': PRESIDENTE_COM_EIC,
                 'Pdte.Cte.NyR': PRESIDENTE_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES,
                 'Mbro.Cte.NyR': MIEMBRO_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES,
                 'Secr.Cte.NyR': SECRETARIO_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES,
                 'Com.Nomb.': COM_NOMB,
                 'Com estrateg': COM_ESTRATEG,
                 'R.C.P.SolMan': R_C_P_SOLMAN,
                 'Sub.General': SUB_GENERAL,
                 'Med.Concusal': MED_CONCUSAL,
                 'Con.Ind.': CON_IND,
                 'MRO.COMS.SEQ': MIEMBRO_COMISION_SEQ,
                 'Tes.Com.Ej.C': TESORERO_COMISION_EJECUTIVA_C,
                 'Sec.Com.EjCR': SECRETARIO_COMISION_EJECUTIVA_CR,
                 'Mie.Com.EjCR': MIEMBRO_COMISION_EJECUTIVA_CR,
                 'PRE.COM.A.YC': PRESIDENTE_COMISION_A_YC,
                 'Promotor': PROMOTOR,
                 'Depositario': DEPOSITARIO,
                 'DEPOSITARIO': DEPOSITARIO,
                 'C.CTR=E.PROM': C_CTR_E_PROM,
                 'INTERVENTOR': INTERVENTOR,
                 'Interventor': INTERVENTOR,
                 'IntervJudic': INTERVENTOR_JUDICIAL,
                 'INTERV.SOLID': INTERVENTOR_SOLIDARIO,
                 'Adm.Sol.Supl': ADMINISTRADOR_SOLIDARIO_SUPLENTE,
                 'PRE.COMS.DEL': PRESIDENTE_COMISION_DELEGADA,
                 'SEC.COMS.DEL': SECRETARIO_COMISION_DELEGADA,
                 'Sec.Com.Del': SECRETARIO_COMISION_DELEGADA,
                 'Con.Del.Com.': CONSEJERO_COMISION_DELEGADA,
                 'Mmbr.Com.Del': MIEMBRO_COMISION_DELEGADA,
                 'MRO.COMS.DEL': MIEMBRO_COMISION_DELEGADA,
                 'Aud.Tit.Grup': AUDITOR_TIT_GRUP,
                 'AUDIT.CONJUN': AUDITOR_CONJUNTO,
                 'AUD.C.C.CONJ': AUDITOR_CUENTAS_CONSOLIDADAS_CONJUNTO,
                 'Miem.Com.Rec': MIEMBRO_COMISION_REC,
                 'Sec.Com.Rec': SECRETARIO_COMISION_REC,
                 'Delegado': DELEGADO,
                 'DELEG.GNERAL': DELEGADO_GENERAL,
                 'P.Com.AyR': PRESIDENTE_COMISION_AYR,
                 'Se.Com.AyR': SECRETARIO_COMISION_AYR,
                 'Miem.ComAyR.': MIEMBRO_COMISION_AYR,
                 'SecCmDirNCon': SEC_CM_DIR_N_CON,
                 'PRE.COMS.O.S': PRESIDENTE_COMISION_O_S,
                 'Pres.Com.O.S': PRESIDENTE_COMISION_O_S,
                 'Vpre.Com.O.S': VICEPRESIDENTE_COMISION_O_S,
                 'Secr.Com.O.S': SECRETARIO_COMISION_O_S,
                 'Vsec.Com.O.S': VICESECRETARIO_COMISION_O_S,
                 'Miem.Com.O.S': MIEMBRO_COMISION_O_S,
                 'MRO.COMS.O.S': MIEMBRO_COMISION_O_S,
                 'S.NO.MI.CO.E': S_NO_MI_CO_E,
                 'Vicsec C.E': VICESECRETARIO_C_E,
                 'SecrComOpVin': SECRETARIO_COMISION_OP_VIN,
                 'SecrComAuCnt': SECRETARIO_COMISION_AU_CNT,
                 'PresComAuCnt': PRESIDENTE_COMISION_AU_CNT,
                 'MiemComAuCnt': MIEMBRO_COMISION_AU_CNT,
                 'Miem.Com.Ri.': MIEMBRO_COMISION_RI,
                 'AdminProvi': ADMINISTRADOR_PROV,
                 'ADM.PROV.SOL': ADMINISTRADOR_PROV_SOLIDARIO,
                 'AdmProvSolEF': ADMINISTRADOR_PROV_SOLIDARIO_EF,
                 'ADJ.GERENCIA': ADJ_GERENCIA,
                 'PRES.HONORI.': PRESIDENTE_HONORIFICO,
                 'Pres. Honor.': PRESIDENTE_HONORIFICO,
                 'Pres.Honorif': PRESIDENTE_HONORIFICO,
                 'V-PRES.HONOR': VICEPRESIDENTE_HONORIFICO,
                 'PreCteAdmres': PRESIDENTE_COMITE_ADM_RES,
                 'Síndico': SINDICO,
                 'SINDICO': SINDICO,
                 'VOC8.CON.REC': VOCAL_8_CON_REC,
                 'VOC10.CON.RE': VOCAL_10_CON_REC,
                 'VOCAL SUPLEN': VOCAL_SUPLENTE,
                 'MBRO.COM.CTO': MIEMBRO_COM_CTO,
                 'V-P1.COM.CTO': VICEPRESIDENTE_PRIMERO_COM_CTO,
                 'V-P2.COM.CTO': VICEPRESIDENTE_SEGUNDO_COM_CTO,
                 'V-S1.COM.CTO': VICESECRETARIO_PRIMERO_COM_CTO,
                 'V-S2.COM.CTO': VICESECRETARIO_SEGUNDO_COM_CTO,
                 'COMS.ACREED.': COMISION_ACREED,
                 'SUPL.COMS.AC': SUPLENTE_COMISION_ACREED,
                 'Pres.J.Adm': PRESIDENTE_J_ADM,
                 'Vpre.J.Adm.': VICEPRESIDENTE_J_ADM,
                 'Secr.J.Adm.': SECRETARIO_J_ADM,
                 'Teso.J.Adm.': TESORERO_J_ADM,
                 'Contador': CONTADOR,
                 'MiemComAuCum': MIEMBRO_COMISION_AU_CUM,
                 'SE.TEC.NO CO': SE_TEC_NO_CO,
                 'MBRO.S.O.CTR': MIEMBRO_S_O_CTR,
                 'Otros': OTROS,
                 'Miem.CTE.CON': MIEMBRO_COMITE_CON,
                 'Pres.C.Pro': PRESIDENTE_COMITE_PRO,
                 'VPre.C.Pro': VICEPRESIDENTE_COMITE_PRO,
                 'Sec.C.Pro': SECRETARIO_COMITE_PRO,
                 'Miem.C.Pro': MIEMBRO_COMITE_PRO,
                 'Mbro.Com.CyA': MIEMBRO_COMISION_CYA,
                 'MRO.COMS.VIG': MIEMBRO_COMISION_VIG,
                 'SUPL.COMS.VI': SUPLENTE_COMISION_VIG,
                 'Ag.Rev.Tit.': AG_REV_TIT,
                 'PRE.C.RIESGO': PRESIDENTE_COMISION_RIESGOS,
                 'V-PRE.COM.RI': VICEPRESIDENTE_COMISION_RIESGOS,
                 'CO.C.RIESGOS': CONSEJERO_COMISION_RIESGOS,
                 'COMS.VIGILAN': COMS_VIGILAN,
                 'Miem.Com.Acr': MIEMBRO_COMISION_ACR,
                 'Fundador': FUNDADOR,
                 'GERENTE SMCP': GERENTE_SMCP,
                 'SUPL.COMS.CT': SUPLENTE_COMISION_CT,
                 'Miem.C.D.C.A': MIEMBRO_CDCA,
                 'Otorgante': OTORGANTE,
                 'SUPL.COMI.LI': SUPLENTE_COMISION_LI,
                 'PRESEN.CONC.': PRESEN_CONC,
                 'Pres.COM.SEG': PRESIDENTE_COMISION_SEG,
                 'Miem.COM.SEG': MIEMBRO_COMISION_SEG,
                 'AUX.ADM.CONC': AUX_ADMINISTRADOR_CONC,
                 'M.C.Com.Perm': MIEMBRO_C_COMISION_PERM,
                 'MANDATARIO': MANDATARIO,

                 # hack
                 'Sociedades beneficiarias': SOCIEDADES_BENEFICIARIAS,
                 'Sociedades fusionadas': SOCIEDADES_FUSIONADAS,
                 }
    KEYWORDS = list(six.viewkeys(_keywords))

    @staticmethod
    def from_string(string):
        return CARGO._keywords[string]
