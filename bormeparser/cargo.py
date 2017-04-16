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

# TODO: COMITE = COMISION

from bormeparser.exceptions import BormeInvalidCargoException


class CARGO:
    PRESIDENTE = "Presidente"
    VICEPRESIDENTE = "Vicepresidente"
    CONSEJERO = "Consejero"
    SECRETARIO = "Secretario"
    VICESECRETARIO = "Vicesecretario"
    CONSEJERO_DELEGADO_MANCOMUNADO = "Consejero delegado mancomunado"
    ADMINISTRADOR_UNICO = "Administrador único"
    MIEMBRO_CONSEJO_RECTOR = "Miembro del consejo rector"
    PRESIDENTE_CONSEJO_RECTOR = "Presidente del consejo rector"
    SECRETARIO_CONSEJO_RECTOR = "Secretario del consejo rector"
    CONSEJERO_CONSEJO_RECTOR = "Consejero del consejo rector"
    ADMINISTRADOR_SOLIDARIO = "Administrador solidario"
    APODERADO = "Apoderado"
    SOCIO_PROFESIONAL = "Socio profesional"
    APODERADO_MANCOMUNADO_SOLIDARIO = "Apoderado mancomunado solidario"
    APODERADO_MANCOMUNADO = "Apoderado mancomunado"
    APODERADO_SOLIDARIO = "Apoderado solidario"
    APODERADO_SOC_UNI = "Apoderado Soc. Uni."  # ?
    CONSEJERO_DELEGADO_MANCOMUNADO_SOLIDARIO = "Consejero delegado mancomunado solidario"
    CONSEJERO_DELEGADO_SOLIDARIO = "Consejero delegado solidario"
    REPRESENTANTE = "Representante"
    CONSEJERO_DELEGADO = "Consejero delegado"
    APODERADO_SOLIDARIO_MANCOMUNADO = "Apoderado solidario mancomunado"
    LIQUISOLI = "Liquidador solidario"
    LIQUIDADOR = "Liquidador"
    APODERADO_SUCURSAL = "Apoderado sucursal"
    REPR_143_RRM = "Representante art. 143 del Reglamento del Registro Mercantil"
    AUDITOR_CUENTAS_CONSOLIDADAS = "Auditor de cuentas consolidadas"
    SECRETARIO_NO_CONSEJERO = "Secretario no consejero"
    VICESECRETARIO_NO_CONSEJERO = "Vicesecretario no consejero"
    AUDITOR = "Auditor"
    ADM_CONCURS = "Administrador concurs."
    REP_ADM_CONC = "Representante administrador concurs."
    AUDITOR_SUPLENTE = "Auditor suplente"
    ADMINISTRADOR_CONJUNTO = "Administrador conjunto"
    ENT_REG_CONT = "Entidad reg. cont."
    ENTIDAD_DEPOSITARIA = "Entidad depositaria"
    CONSEJERO_DOMINIC = "Consejero dominic."
    CONSEJERO_EJECUTIVO = "Consejero ejecutivo"
    MIEMBRO_COMIT_AUD = "Miembro de la comisión Aud."
    SECRETARIO_COMIT_AUD = "Secretario de la comisión Aud."
    PRESIDENTE_COMIT_AUD = "Presidente de la comisión Aud."
    PRESIDENTE_COMISION_CONTROL = "Presidente de la comisión de control"
    SECRETARIO_COMISION_CONTROL = "Secretario de la comisión de control"
    MIEMBRO_COMISION_CONTROL = "Miembro de la comisión de control"
    RLC_PERMA = "Representante perma."
    LIQUIDADOR_MANCOMUNADO = "Liquidador mancomunado"
    MIEMBRO_COMISION_EJECUTIVA = "Miembro de la comisión ejecutiva"
    PRESIDENTE_JGPV = "Presidente J.G.P.V."
    SECRETARIO_JGPV = "Secretario J.G.P.V."
    MIEMBRO_JGPV = "Miembro J.G.P.V."
    TESORERO = "Tesorero"
    COMISARIO = "Comisario"
    SOCIO_UNICO = "Socio único"
    SOCIEDADES_BENEFICIARIAS = "Sociedades beneficiarias"
    SOCIEDADES_FUSIONADAS = "Sociedades fusionadas"
    GERENTE = "Gerente"
    GERENTE_ADJUNTO = "Gerente adjunto"
    LIQUIDADOR_UNICO = "Liquidador único"
    ENTIDAD_GESTORA = "Entidad gestora"
    AUDITOR_TITU = "Auditor titular"
    AUDITOR_CUENTAS = "Auditor de cuentas"
    DIRECTOR_GENERAL = "Director general"
    MIEMBRO_JUNTA_DIRECTIVA = "Miembro de la Junta Directiva"
    SECRETARIO_JUNTA_DIRECTIVA = "Secretario de la Junta Directiva"
    SOCIO = "Socio"
    COMS_DEL_INV = "Comisión del inv."
    PRESIDENTE_COMS_D_I = "Presidente de la comisión de inv."
    S_N_C_C_D_I = "Secretario no consejero de la comisión de inv."
    VS_N_C_C_D_I = "Vicesecretario no consejero de la comisión de inv."
    MIEMBRO_COMITE_INV = "Miembro del comité inv."
    NO_DEFINIDO = "No definido"  # ?
    LETRADO_ASESOR = "Letrado asesor"
    EXP_IND = "Exp. ind."  # Experto independiente?
    MIEMBRO_COMISION_LIQ = "Miembro de la comisión liq."
    PRESIDENTE_COMISION_LIQ = "Presidente de la comisión liq."
    SECRETARIO_COMISION_LIQ = "Secretario de la comisión liq."
    GER_COMISION_GER = "Gerente de la comision ger."  # ?
    ADMINISTRADOR = "Administrador"
    VOCAL_JUNTA_DIRECTIVA = "Vocal de la Junta Directiva"
    VOCAL_SECUNDARIO_JUNTA_DIRECTIVA = "Vocal secundario de la Junta Directiva"
    VICEPRESIDENTE_JUNTA_DIRECTIVA = "Vicepresidente de la Junta Directiva"
    VICEPRESIDENTE_SEGUNDO_JUNTA_DIRECTIVA = "Vicepresidente segundo de la Junta Directiva"
    TESORERO_JUNTA_DIRECTIVA = "Tesorero de la Junta Directiva"
    DIRECTOR = "Director"
    VICEDIRECTOR = "Vicedirector"
    DEF_PARTICIP = "Def. particip"  # ?
    ADM_JUDICIAL = "Administrador judicial"
    ADM_SUPLENTE = "Administrador suplente"
    APODERADO_D_GENERAL = "Apoderado D. general"
    COM_AUDIT = "Miembro del comité de aud."  # ?
    REPR_PERMAN = "Representación permananente"
    GERENTE_UNI = "Gerente uni."
    DIRECTOR_TECNICO = "Director técnico"
    MIEMBRO_JUNTA_RECTORA = "Miembro de la Junta Rectora"
    SECRETARIO_JUNTA_RECTORA = "Secretario de la Junta Rectora"
    PRESIDENTE_JUNTA_RECTORA = "Presidente de la Junta Rectora"
    VICEPRESIDENTE_JUNTA_RECTORA = "Vicepresidente de la Junta Rectora"
    LIQUIDADOR_JUDICIAL = "Liquidador judicial"
    RLC_PER_S = "R.L.C.Per.S."  # Representante
    VICEPRESIDENTE_CONSEJO_RECTOR = "Vicepresidente del consejo rector"
    COMISION_EJECUTIVA = "Comisión ejecutiva"
    AUDITOR_GRUP = "Auditor Grup"  # ?
    PRESIDENTE_COMISION_EJECUTIVA = "Presidente de la comisión ejecutiva"
    COPRESIDENTE_COMISION_EJECUTIVA = "Copresidente de la comisión ejecutiva"
    VICEPRESIDENTE_COMISION_EJECUTIVA = "Vicepresidente de la comisión ejecutiva"
    VICEPRESIDENTE_PRIMERO = "Vicepresidente primero"
    AUDITOR_SU_C_CON = "Auditor suplente C.Con"  # ?
    MIEMBRO_CONSEJO_DIRECTIVO = "Miembro del consejo directivo"
    PRESIDENTE_CONSEJO_DIRECTIVO = "Presidente del consejo directivo"
    VICEPRESIDENTE_CONSEJO_DIRECTIVO = "Vicepresidente del consejo directivo"
    COMI_SIN_OBLI = "ComiSinObli"  # ?
    MIEMBRO_COMISION_NOM_RE = "Miembro de la comisión Nom.Re."  # ?
    MIEMBRO_COMISION_DIRECTIVA = "Miembro de la comisión directiva"
    SECRETARIO_COMISION_DIRECTIVA = "Secretario de la comisión directiva"
    PRESIDENTE_COMISION_DIRECTIVA = "Presidente de la comisión directiva"
    SUPLENTE = "Suplente"
    COMISARIO_SI_O = "COMISAR.SI.O"  # ?
    COMISARIO_SUP_S = "COMISR.SUP.S"  # ?
    AUDITOR_MANCOMUNADO = "Auditor mancomunado"
    MIEMBRO_COM_EIC = "Miembro de la comisión EIC"  # ?
    MIEMBRO_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES = "Miembro del comité de Nombramientos y Retribuciones"  # NyR
    APODERADO_CONJUNTO = "Apoderado conjunto"
    R_C_P_SOLMAN = "R.C.P.SolMan"  # ?
    REPRESENTANTE_SUCURS = "Representante de la sucursal"
    MEDIAD_CONCUSAL = 'Med.Concusal'  # ?
    LIQUIDADOR_CONC = 'Liquidador conc.'  # ?
    DIRECTOR_GENERAL_SUPLENTE = "Director general suplente"
    CONSEJERO_IND_COOR = 'Consejero independiente Coor.'  # ?
    CONSEJERO_COOR = "Consejero Coor."  # ?
    CONSEJERO_COOR_CA = "Consejero Coor. Ca."  # ?
    ADMINISTRADOR_MANCOMUNADO = "Administrador mancomunado"
    PRESIDENTE_JUNTA_DIRECTIVA = "Presidente de la Junta Directiva"
    DIRECTOR_SUCURSAL = "Director de la sucursal"
    MIEMBRO_COMISION_SEQ = "Miembro de la comisión Seq."
    TESORERO_CONSEJO_RECTOR = "Tesorero del consejo rector"
    TESORERO_COMISION_EJECUTIVA_C = "Tesorero de la comisión ejecutiva C."  # ?
    MIEMBRO_COMISION_EJECUTIVA_CR = "Miembro de la comisión ejecutiva CR."  # ?
    PRESIDENTE_COMISION_A_YC = "Presidente de la comisión A.YC."
    PROMOTOR = "Promotor"
    DEPOSITARIO = "Depositario"
    VOCAL_COMIT_AUD = "Vocal Comit. Aud."
    DIRECTOR_FABRICA = "Director fábrica"
    C_CTR_E_PROM = 'C.CTR=E.PROM'
    INTERVENTOR = "Interventor"
    INTERVENTOR_JUDICIAL = "Interventor judicial"
    ADMINISTRADOR_SOLIDARIO_SUPLENTE = "Administrador solidario suplente"
    AUDITOR_SUPLENTE_CUENTAS_CONSOLIDADAS = "Auditor suplente cuentas consolidadas"
    ENTIDAD_COGESTORA = "Entidad cogestora"
    VICEPRESIDENTE_JGPV = "Vicepresidente J.G.P.V."
    PRESIDENTE_COMISION_INV = "Presidente de la comisión Inv."
    VICEPRESIDENTE_COMISION_INV = "Vicepresidente de la comisión Inv."
    SECRETARIO_COMISION_INV = "Secretario de la comisión Inv."
    VICESECRETARIO_COMISION_INV = "Vicesecretario de la comisión Inv."
    SECRETARIO_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES = "Secretario del comité de Nombramientos y Retribuciones"
    DIRECTOR_GENERAL_ADJUNTO = "Director general adjunto"
    PRESIDENTE_COMISION_DELEGADA = "Presidente de la comisión delegada"
    SECRETARIO_COMISION_DELEGADA = "Secretario de la comisión delegada"
    VICESECRETARIO_COMISION_DELEGADA = "Vicesecretario de la comisión delegada"
    MIEMBRO_COMISION_DELEGADA = "Miembro de la comisión delegada"
    AUDITOR_TIT_GRUP = "Auditor Titular Grup."
    AUDITOR_CONJUNTO = "Auditor conjunto"
    AUDITOR_CONS = "Auditor Cons."  # ?
    AUDITOR_CUENTAS_CONSOLIDADAS_CONJUNTO = "Auditor de cuentas consolidadas conjunto"
    MIEMBRO_COMITE_REC = "Miembro del comité Rec."
    SECRETARIO_COMITE_REC = "Secretario del comité Rec."
    VICESECRETARIO_COMITE_REC = "Vicesecretario del comité Rec."
    DELEGADO = "Delegado"
    VOCAL_E_P_JUNTA_DIRECTIVA = "Vocal E.P. Junta Directiva"  # ?
    PRESIDENTE_COMISION_AYR = "Presidente de la comisión AyR"  # ?
    MIEMBRO_COMISION_AYR = "Miembro de la comisión AyR"  # ?
    SEC_CM_DIR_N_CON = 'SecCmDirNCon'  # ?
    SECRETARIO_COMISION_O_S = "Secretario de la comisión O.S."
    MIEMBRO_COMISION_O_S = "Miembro de la comisión O.S."
    VICEPRESIDENTE_COMISION_O_S = "Vicepresidente de la comisión O.S."
    VICESECRETARIO_COMISION_O_S = "Vicesecretario de la comisión O.S."
    PRESIDENTE_COMISION_O_S = "Presidente de la comisión O.S."
    CONSEJERO_SUPLENTE = "Consejero suplente"
    S_NO_MI_CO_E = 'S.NO.MI.CO.E'  # ?
    SOCIO_GESTOR = "Socio gestor"
    VICESECRETARIO_C_E = "Vicesecretario C.E"  # ?
    SECRETARIO_COMISION_OP_VIN = "Secretario de la comisión OpVin."  # ?
    SECRETARIO_COMISION_AU_CNT = "Secretario de la comisión Au.Cnt."  # Auditoria de cuentas?
    ADMINISTRADOR_PROV_SOLIDARIO = "Administrador Prov.Sol."
    CONSEJERO_INTERIN = "Consejero Interin."
    ADJ_GERENCIA = "Adj. Gerencia"
    PRESIDENTE_HONORIFICO = "Presidente honorífico"
    PRESIDENTE_COMITE_ADM_RES = "Presidente del comité Adm.Res."  # ?
    REPRESENTANTE_FISCAL = "Representante fiscal"
    PRESIDENTE_EJECUTIVO = "Presidente ejecutivo"
    ADMINISTRADOR_MANCOMUNADO_SUPLENTE = "Administrador mancomunado suplente"
    VICESECRETARIO_COMISION_CONTROL = "Vicesecretario de la comisión de control"
    DIRECTOR_ADMINIS = "Director Adminis."  # ?
    SUBDIRECTOR_GENERAL = "Subdirector general"
    MIEMBRO_COMISION_GER = "Miembro de la comisión Ger."  # ?
    ADMINISTRADOR_ADJUNTO = "Administrador adjunto"
    VICESECRETARIO_JUNTA_DIRECTIVA = "Vicesecretario de la Junta Directiva"
    COM_AUDIT_CTRL = "Comisión Aud.Ctrl."
    MIEMBRO_COM_AUD = "Miembro de la comisión Aud."
    SECRETARIO_COMISION_EJECUTIVA = "Secretario de la comisión ejecutiva"
    SECRETARIO_COMISION_EJECUTIVA_NO_CONSEJERO = "Secretario de la comisión ejecutiva no consejero"
    PRESIDENTE_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES = "Presidente del comité de Nombramientos y Retribuciones"
    MIEMBRO_COMISION_AU_CNT = "Miembro de la comisión Au.Cnt."
    SINDICO = "Síndico"
    SUPLENTE_CONSEJO_RECTOR = "Suplente del consejo rector"
    D_G_CONSEJO_RECTOR = "D.G. del consejo rector"  # director general?
    SECRETARIO_NO_CONSEJERO_GO = "Secretario no consejero Go."  # ?
    MIEMBRO_CONSEJERO_GO = "Miembro consejero Go."  # ?
    VICEPRESIDENTE_COMISION_CONTROL = "Vicepresidente de la comisión de control"
    SUPLENTE_COMISION_CONTROL = "Suplente de la comisión de control"
    MIEMBRO_AGPV = "Miembro A.G.P.V."  # ?
    VOCAL_3_JUNTA_DIRECTIVA = "Vocal 3 de la Junta Directiva"
    VOCAL_4_JUNTA_DIRECTIVA = "Vocal 4 de la Junta Directiva"
    MIEMBRO_COM_CTO = "Miembro de la comisión Cto."  # ?
    VICEPRESIDENTE_PRIMERO_COM_CTO = "Vicepresidente primero de la comisión Cto."
    VICEPRESIDENTE_SEGUNDO_COM_CTO = "Vicepresidente segundo de la comisión Cto."
    VICESECRETARIO_PRIMERO_COM_CTO = "Vicepresecretario primero de la comisión Cto."
    VICESECRETARIO_SEGUNDO_COM_CTO = "Vicepresecretario segundo de la comisión Cto."
    COMISION_ACREEDORES = "Comisión de acreedores"
    SUPLENTE_COMISION_ACREEDORES = "Suplente de la comisión de acreedores"
    MIEMBRO_COMISION_ACREEDORES = "Miembro de la comisión de acreedores"
    PRESIDENTE_COM_EIC = "Presidente de la comisión EIC"
    COPRESIDENTE = "Copresidente"
    VICESECRETARIO_CONSEJO_RECTOR = "Vicesecretario del consejo rector"
    SOCIO_COLECTIVO = "Socio colectivo"
    DIRECTOR_COMERCIAL = "Director comercial"
    SECRETARIO_COMISION_EJECUTIVA_CR = "Secretario de la comisión ejecutiva CR."  # ?
    PRESIDENTE_J_ADM = "Presidente J.Adm."
    VICEPRESIDENTE_J_ADM = "Vicepresidente J.Adm."
    SECRETARIO_J_ADM = "Secretario J.Adm."
    TESORERO_J_ADM = "Tesorero J.Adm."
    CONTADOR = "Contador"
    PRESIDENTE_COMISION_DIRECTIVA = "Presidente de la comisión directiva"
    PRESIDENTE_COMISION_AU_CNT = "Presidente de la comisión Au.Cnt."
    MIEMBRO_COMISION_AU_CUM = "Miembro de la comisión Au.Cnt."
    SE_TEC_NO_CO = 'SE.TEC.NO CO'  # ?
    MIEMBRO_S_O_CTR = 'Miembro S.O.CTR'  # ?
    PRESIDENTE_COM_AUD = "Presidente de la comisión Aud."
    OTROS = "Otros"
    LIQUIDADOR_SUPLENTE = "Liquidador suplente"
    CONSEJERO_HONORA = "Consejero honora."
    DIRECTOR_GENERAL_ADM = "Director general Adm."
    GERENTE_EJECUTIVO = "Gerente ejecutivo"
    ADMINISTRADOR_PROV_SOLIDARIO_EF = "Administrador Prov.Sol.E.F."
    MIEMBRO_COMITE_CON = "Miembro del comité Con."
    PRESIDENTE_COMITE_PRO = "Presidente del comité Pro."
    VICEPRESIDENTE_COMITE_PRO = "Vicepresidente del comité Pro."
    SECRETARIO_COMITE_PRO = "Secretario del comité Pro."
    MIEMBRO_COMITE_PRO = "Miembro del comité Pro."
    SECRETARIO_GENERAL = "Secretario general"
    DIRECTOR_EJECUTIVO = "Director ejecutivo"
    SOCIO_UNICO_PROFESIONAL = "Socio único profesional"
    VICEPRESIDENTE_SEGUNDO = "Vicepresidente segundo"
    SECRETARIO_GENERAL_ADJUNTO = "Secretario general adjunto"
    VICESECRETARIO_NO_CONSEJERO_SEGUNDO = "Vicesecretario no consejero segundo"
    MIEMBRO_COMISION_RETR = "Miembro de la comisión Retr."
    ADMINISTRADOR_PRIMERO = "Administrador primero"
    REPRESENTANTE_PLAN = "Representante Plan."
    REPRESENTANTE_SUPLENTE = "Representante suplente"
    CONSEJERO_INDEPENDIENTE = "Consejero independiente"
    DEPOSITARIO_COMISION_CONTROL = "Depositario de la comisión de control"
    ENTIDAD_GESTORA_ACT = "Entidad gestora Act."  # ?
    ENTIDAD_GESTORA_DEL = "Entidad gestora Del."  # ?
    ENTIDAD_GESTORA_INDEPENDIENTE = "Entidad gestora independiente"
    DIRECTOR_DEPARTAMENTO = "Director de departamento"
    DIRECTOR_EXPLOTA = "Director Explota."  # ?
    DIRECTOR_FINANCIERO = "Director financiero"
    SUBDIRECTOR = "Subdirector"
    SECRETARIO_NO_CONSEJERO_COMISION_EJECUTIVA = "Secretario no consejero de la comisión ejecutiva"
    INTERVENTOR_SOLIDARIO = "Interventor solidario"
    VOCAL_SUPLENTE = "Vocal suplente"
    VICEPRESIDENTE_HONORIFICO = "Vicepresidente honorífico"
    VICEPRESIDENTE_COMISION_DIRECTIVA = "Vicepresidente de la comisión directiva"
    MIEMBRO_COMISION_CYA = "Miembro de la comisión CyA"
    MIEMBRO_COMISION_VIG = "Miembro de la comisión VIG"
    SUPLENTE_COMISION_VIG = "Suplente de la comisión VIG"
    AG_REV_TIT = 'Ag.Rev.Tit.'  # ?
    PRESIDENTE_COMISION_RIESGOS = "Presidente de la comisión de riesgos"
    VICEPRESIDENTE_COMISION_RIESGOS = "Vicepresidente de la comisión de riesgos"
    CONSEJERO_COMISION_RIESGOS = "Consejero de la comisión de riesgos"
    COMS_VIGILAN = 'Coms.Vigilan'  # ?
    FUNDADOR = "Fundador"
    GERENTE_SMCP = "Gerente SMCP"  # ?
    SUPLENTE_COMISION_CT = "Suplente de la comisión CT"  # ?
    MIEMBRO_CDCA = "Miembro C.D.C.A."  # ?
    OTORGANTE = "Otorgante"
    SUPLENTE_COMISION_LIQ = "Suplente de la comisión liq."  # ?
    PRESEN_CONC = "Presen. Conc."  # ?
    PRESIDENTE_COMISION_SEGUIMIENTO = "Presidente de la comisión de seguimiento"
    MIEMBRO_COMISION_SEGUIMIENTO = "Miembro de la comisión de seguimiento"
    AUX_ADMINISTRADOR_CONC = 'Aux. Adm. Conc.'  # ?
    MIEMBRO_C_COMISION_PERM = "Miembro C. comisión perm."  # ?
    MANDATARIO = "Mandatario"
    CONSEJERO_COMISION_DELEGADA = "Consejero de la comisión delegada"
    ADMINISTRADOR_PROV = "Administrador prov."
    SECRETARIO_COMISION_AYR = "Secretario de la comisión AyR"  # ?
    DELEGADO_GENERAL = "Delegado general"
    ENTIDAD_ENC_GESTORA = "Entidad enc. gestora"  # ?
    COMISION_CONTROL_Y_S = "Comisión de control y S."  # ?
    PRESIDENTE_ASAM_SO = "Presidente Asam. So."  # ?
    MIEMBRO_COMISION_MIX = "Miembro de la comisión mix."  # ?
    GESTOR = "Gestor"
    ENTIDAD_PROMOTORA = "Entidad promotora"
    ME_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES = "Me. del comité de Nombramientos y Retribuciones"  # ?
    CENSOR_CUENT = "Censor Cuent"  # ?
    SOCIO_GEST_ACT = "Socio gest. act."  # ?
    SOCIO_HONORIFICO = "Socio honorífico"
    OBSER_CON_AD = "Obser. Con. Ad."  # ?
    MIEMBRO_COMISION = "Miembro de la comisión"
    MIEMBRO_COMISION_INDEPENDIENTE = "Miembro de la comisión independiente"
    SECRETARIO_ADJUNTO = "Secretario adjunto"
    SECRETARIO_ACTAS = "Secretario actas"
    VICESECRETARIO_PRIMERO_NO_CONSEJERO = "Vicesecretario primero no consejero"
    VICESECRETARIO_SEGUNDO_NO_CONSEJERO = "Vicesecretario segundo no consejero"
    VOCAL_4_CONSEJO_RECTOR = "Vocal 4 del consejo rector"
    VOCAL_6_CONSEJO_RECTOR = "Vocal 6 del consejo rector"
    VOCAL_8_CONSEJO_RECTOR = "Vocal 8 del consejo rector"
    VOCAL_10_CONSEJO_RECTOR = "Vocal 10 del consejo rector"
    SUPLENTE_3_CONSEJO_RECTOR = "Suplente 3 del consejo rector"
    LIQUIDADOR_DEL_MANCOMUNADO = "Liquidador del. mancomunado"  # delegado?
    AUDITOR_CUENTAS_CONSOLIDADAS_SUPLENTE = "Auditor de cuentas consolidadas suplente"
    COMISION_CONTROL = "Comisión de control"
    VICETESORERO = "Vicetesorero"
    VICETESORERO_JUNTA_DIRECTIVA = "Vicetesorero de la Junta Directiva"
    DIRECTOR_GENERAL_FINANCIERO = "Director general financiero"
    COMISION_LIQ = "Comisión liq."
    VICESECRETARIO_SEGUNDO_JUNTA_DIRECTIVA = "Vicesecretario segundo de la Junta Directiva"
    VOCAL_2_JUNTA_DIRECTIVA = "Vocal 2 de la Junta Directiva"
    CONTAD_JUNTA_DIRECTIVA = "Contador de la Junta Directiva"
    PRESIDENTE_COMISION_AUDIT = "Presidente de la comisión audit."  # auditora?
    MIEMBRO_COMISION_AUDIT = "Miembro de la comisión audit."  # auditora?
    SECRETARIO_COMISION_AUDIT = "Secretario de la comisión audit."  # auditora?
    VOCAL_JUNTA_RECTORA = "Vocal de la Junta Rectora"
    COMISION_NOMB = "Comisión de nombramientos"
    COMISION_ESTRATEG = "Comisión estratégica"
    MIEMBRO_COMISION_ESTRATEG = "Miembro de la comisión estratégica"
    INTERVENTOR_SUSPG = "Interventor Suspg."  # ?
    VOCAL = "Vocal"
    MIEMBRO_J_ADM = "Miembro J. Adm."
    PRESIDENTE_COMISION_AU_CUM = "Presidente de la comisión Au.Cum."  # ?
    MIEMBRO_COMISION_RIESGOS = "Miembro de la comisión de riesgos"
    COMISION_SEGUIMIENTO = "Comisión de seguimiento"
    SECRETARIO_GCA = "Secretario G.C.A."  # ?
    PRESIDENTE_JUNTA = "Presidente Junta"
    SECRETARIO_JUNTA = "Secretario Junta"
    MIEMBRO_COMITE_CF = "Miembro del comité CF"  # ?
    SECRETARIO_NO_MIEN = "Secretario no mien."  # ?
    VICEPRESIDENTE_COMIT_AUD = "Vicepresidente del comité aud."  # ?
    SUPLENTE_CONSEJO_ADMINISTRACION = "Suplente del consejo de administración"
    GERENTE_SUCURSAL = "Gerente de la sucursal"
    PRESIDENTE_GESTOR = "Presidente gestor"
    VOCAL_1 = "Vocal 1"
    VOCAL_2 = "Vocal 2"
    PRESIDENTE_COMISION_GESTORA = "Presidente de la comisión gestora"
    MI_O_C_C = "Mi. o. c. c."  # ?
    MIEMBRO_COM_ASESO = "Miembro del comité asesor"  # ?
    PRESIDENTE_COMISION_ANR = "Presidnete de la comisión ANR"  # ?
    COM_CONS_FAM = "Com. Cons. Fam."  # ?
    MIEMBRO_COMISION_SEG_FO = "Miembro de la comisión Seg. Fo."  # ?
    COM_GERENCIA = "Com. Gerencia"  # ?
    VICEPRESIDENTE_TERCERO = "Vicepresidente tercero"
    SECRETARIO_SUPLENTE = "Secretario suplente"
    SECRETARIO_SUPLENTE_NO_CONSEJERO = "Secretario suplente no consejero"
    VICESECRETARIO_PRIMERO = "Vicesecretario primero"
    VICESECRETARIO_TERCERO_NO_CONSEJERO = "Vicesecretario tercero no consejero"
    CONSEJERO_DELEGADO_SUPLENTE = "Consejero delegado suplente"
    CONSEJERO_DELEGADO_JUN = "Consejero delegado jun."  # ?
    VOCAL_3_CONSEJO_RECTOR = "Vocal 3 del consejo rector"
    DIRECTOR_MARKETING = "Director de marketing"
    DIRECTOR_RELACIONES_LABORALES = "Director de relaciones laborales"
    DIRECTOR_OPERACIONES = "Director operaciones"
    DIRECTOR_RECURSOS_HUMANOS = "Director de Recursos Humanos"
    VOCAL_6_JUNTA_DIRECTIVA = "Vocal 6 de la Junta Directiva"
    VOCAL_7_JUNTA_DIRECTIVA = "Vocal 7 de la Junta Directiva"
    VOCAL_10_JUNTA_DIRECTIVA = "Vocal 10 de la Junta Directiva"
    VICESECRETARIO_COMISION_EJECUTIVA = "Vicesecretario de la comisión ejecutiva"
    MIEMBRO_SUPLENTE_COMITE_REC = "Miembro suplente del comité rec."  # ?
    MIEMBRO_COMISION_RESPO = "Miembro de la comisión respo."  # ?
    PRESIDENTE_COMISION_RESPO = "Presidente de la comisión respo."  # ?
    CONSEJERO_EXT_DOM = "Consejero externo Dom."  # ?
    CONSEJERO_OTR_EXT = "Consejero Otr. externo"  # ?
    CONSEJERO_EXTERNO = "Consejero externo"
    PRESIDENTE_SUPLENTE = "Presidente suplente"
    MIEMBRO_COMISION_CONSU = "Miembro de la comisión Consu."  # ?
    MIEMBRO_COMISION_REP_MUNI = "Miembro de la comisión Rep. Muni."  # ?

    _keywords = {'Presidente': PRESIDENTE,
                 'PRESIDENTE': PRESIDENTE,
                 'Pdte.': PRESIDENTE,
                 'PresEjecutiv': PRESIDENTE_EJECUTIVO,
                 'PRES.EJECUT.': PRESIDENTE_EJECUTIVO,
                 'Pres. Sup': PRESIDENTE_SUPLENTE,
                 'PRESI.GEST.': PRESIDENTE_GESTOR,
                 'COPRESIDENTE': COPRESIDENTE,
                 'Vicepresid.': VICEPRESIDENTE,
                 'VICEPRESIDEN': VICEPRESIDENTE,
                 'Vicepresiden': VICEPRESIDENTE,
                 'Vicepresi.1º': VICEPRESIDENTE_PRIMERO,
                 'VICEPRESID.1': VICEPRESIDENTE_PRIMERO,
                 'Vicepr.1': VICEPRESIDENTE_PRIMERO,
                 'VICEPRESID.2': VICEPRESIDENTE_SEGUNDO,
                 'Vicepr.2': VICEPRESIDENTE_SEGUNDO,
                 'Vicepr.3': VICEPRESIDENTE_TERCERO,
                 'Consejero': CONSEJERO,
                 'Cons.': CONSEJERO,
                 'Consj.Domini': CONSEJERO_DOMINIC,
                 'CONS.DOMINIC': CONSEJERO_DOMINIC,
                 'Secretario': SECRETARIO,
                 'SECRETARIO': SECRETARIO,
                 'SECR.ADJUNTO': SECRETARIO_ADJUNTO,
                 'Sec.Actas': SECRETARIO_ACTAS,
                 'Secr.Supl.': SECRETARIO_SUPLENTE,
                 'Secr.Sup.noC': SECRETARIO_SUPLENTE_NO_CONSEJERO,
                 'Secret.Gral.': SECRETARIO_GENERAL,
                 'Secr.Gral.Ad': SECRETARIO_GENERAL_ADJUNTO,
                 'SECR.NO.MIEN': SECRETARIO_NO_MIEN,
                 'Vicesecret.': VICESECRETARIO,
                 'VICESECRET.': VICESECRETARIO,
                 'VICESECRET.1': VICESECRETARIO_PRIMERO,
                 'VsecrNoConsj': VICESECRETARIO_NO_CONSEJERO,
                 'V-SEC NO CON': VICESECRETARIO_NO_CONSEJERO,
                 'Vcsec.no.Con': VICESECRETARIO_NO_CONSEJERO,
                 'V- SEC NO CON': VICESECRETARIO_NO_CONSEJERO,
                 'Vsecr1.NC': VICESECRETARIO_PRIMERO_NO_CONSEJERO,
                 'V-SEC.NO.C.2': VICESECRETARIO_SEGUNDO_NO_CONSEJERO,
                 'Vsecr2.NC': VICESECRETARIO_SEGUNDO_NO_CONSEJERO,
                 'Vsecr3.NC': VICESECRETARIO_TERCERO_NO_CONSEJERO,
                 'Cons.Del.Man': CONSEJERO_DELEGADO_MANCOMUNADO,
                 'CONS.DEL.MAN': CONSEJERO_DELEGADO_MANCOMUNADO,
                 'Con.Del.manc': CONSEJERO_DELEGADO_MANCOMUNADO,
                 'Con.Del.Sup': CONSEJERO_DELEGADO_SUPLENTE,
                 'Cons.Del.Jun': CONSEJERO_DELEGADO_JUN,
                 'CONS.OTR.EXT': CONSEJERO_OTR_EXT,
                 'Cons.Externo': CONSEJERO_EXTERNO,
                 'Vcs.Cons.Rec': VICESECRETARIO_CONSEJO_RECTOR,
                 'Mie.Cons.Rec': MIEMBRO_CONSEJO_RECTOR,
                 'Miem.Co.Rec': MIEMBRO_CONSEJO_RECTOR,
                 'Miem.Co.Rec.': MIEMBRO_CONSEJO_RECTOR,
                 'Miem.C.Ret': MIEMBRO_CONSEJO_RECTOR,
                 'M.Com.Retr.': MIEMBRO_COMISION_RETR,
                 'MBRO.COM.RET': MIEMBRO_COMISION_RETR,
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
                 'CONS.RECTOR': CONSEJERO_CONSEJO_RECTOR,
                 'Cons.Del.C.R': CONSEJERO_CONSEJO_RECTOR,
                 'D.G.Cons.Rec': D_G_CONSEJO_RECTOR,
                 'VOC3.CON.REC': VOCAL_3_CONSEJO_RECTOR,
                 'VOC4.CON.REC': VOCAL_4_CONSEJO_RECTOR,
                 'VOC6.CON.REC': VOCAL_6_CONSEJO_RECTOR,
                 'VOC8.CON.REC': VOCAL_8_CONSEJO_RECTOR,
                 'VOC10.CON.RE': VOCAL_10_CONSEJO_RECTOR,
                 'SUPL3.CON.RE': SUPLENTE_3_CONSEJO_RECTOR,
                 'Adm. Unico': ADMINISTRADOR_UNICO,
                 'Adm. Unico.': ADMINISTRADOR_UNICO,
                 'Adm. unico': ADMINISTRADOR_UNICO,
                 'ADM.UNICO': ADMINISTRADOR_UNICO,
                 'Admin.Unico': ADMINISTRADOR_UNICO,
                 'Admin.Unico.': ADMINISTRADOR_UNICO,
                 'Adm. Unico 2': ADMINISTRADOR_UNICO,
                 'DM.UNICO 2': ADMINISTRADOR_UNICO,
                 'Adm. Solid.': ADMINISTRADOR_SOLIDARIO,
                 'ADM.SOLIDAR.': ADMINISTRADOR_SOLIDARIO,
                 'Admin.Solid': ADMINISTRADOR_SOLIDARIO,
                 'Adm. Solida.': ADMINISTRADOR_SOLIDARIO,
                 'ADM.CONCURS.': ADM_CONCURS,
                 'Adm.Concur': ADM_CONCURS,
                 'Admin.Conc': ADM_CONCURS,
                 'Adm. Mancom': ADMINISTRADOR_MANCOMUNADO,
                 'Admin.Manc': ADMINISTRADOR_MANCOMUNADO,
                 'ADM.CONJUNTO': ADMINISTRADOR_CONJUNTO,
                 'Adm. Mancom.': ADMINISTRADOR_MANCOMUNADO,
                 'Adm. Manco.': ADMINISTRADOR_MANCOMUNADO,
                 'Adm. Manco': ADMINISTRADOR_MANCOMUNADO,
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
                 'APODERAD.SOL': APODERADO_SOLIDARIO,
                 'APOD.SUCURSA': APODERADO_SUCURSAL,
                 'APOD.CONJUN.': APODERADO_CONJUNTO,
                 'Apo.D.Gral.': APODERADO_D_GENERAL,
                 'Apod.D.Gral.': APODERADO_D_GENERAL,
                 'APOD.SOL/MAN': APODERADO_SOLIDARIO_MANCOMUNADO,
                 'Apod.Sol-man': APODERADO_SOLIDARIO_MANCOMUNADO,
                 'Apo.Soc.Uni.': APODERADO_SOC_UNI,
                 'Soc.Prof.': SOCIO_PROFESIONAL,
                 'Soc.Uni.Prof': SOCIO_UNICO_PROFESIONAL,
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
                 'REPR. SUPLT.': REPRESENTANTE_SUPLENTE,
                 'Con.Delegado': CONSEJERO_DELEGADO,
                 'CONS. DELEG.': CONSEJERO_DELEGADO,
                 'Cons.Delegad': CONSEJERO_DELEGADO,
                 'Cons.Ext.Dom': CONSEJERO_EXT_DOM,
                 'CONS.EJECUTI': CONSEJERO_EJECUTIVO,
                 'Consejero Ej': CONSEJERO_EJECUTIVO,
                 'Liquidador': LIQUIDADOR,
                 'LIQUIDADOR': LIQUIDADOR,
                 'Liq.Sup.': LIQUIDADOR_SUPLENTE,
                 'LIQUID.SUPL.': LIQUIDADOR_SUPLENTE,
                 'LiquiSoli': LIQUISOLI,
                 'LiqSolid': LIQUISOLI,
                 'Liquidador M': LIQUIDADOR_MANCOMUNADO,
                 'LiqManc': LIQUIDADOR_MANCOMUNADO,
                 'LIQUID.MANC.': LIQUIDADOR_MANCOMUNADO,
                 'Liquid.manc': LIQUIDADOR_MANCOMUNADO,
                 'Liq.del.man': LIQUIDADOR_DEL_MANCOMUNADO,
                 'LIQ.CONC.': LIQUIDADOR_CONC,
                 'Liquid.conc.': LIQUIDADOR_CONC,
                 'LiqC': LIQUIDADOR_CONC,
                 'LiqUnico': LIQUIDADOR_UNICO,
                 'Liqid.Unic': LIQUIDADOR_UNICO,
                 'Liq.Judicial': LIQUIDADOR_JUDICIAL,
                 'REPR.143 RRM': REPR_143_RRM,
                 'CONSEJERO': CONSEJERO,
                 'ConsejSuplen': CONSEJERO_SUPLENTE,
                 'Consj. Supl.': CONSEJERO_SUPLENTE,
                 'CONS.SUPLENT': CONSEJERO_SUPLENTE,
                 'Cons.Interin': CONSEJERO_INTERIN,
                 'CONS.HONORA.': CONSEJERO_HONORA,
                 'Cons. Idpte.': CONSEJERO_INDEPENDIENTE,
                 'Con.Ind.': CONSEJERO_INDEPENDIENTE,
                 'CONS.INDEPEN': CONSEJERO_INDEPENDIENTE,
                 'CON.INDEPEND': CONSEJERO_INDEPENDIENTE,
                 'Con.Ind.Coor': CONSEJERO_IND_COOR,
                 'Consej.Coord': CONSEJERO_COOR,
                 'CONS.COOR.CA': CONSEJERO_COOR_CA,
                 'CONS.DEL.M/S': CONSEJERO_DELEGADO_MANCOMUNADO_SOLIDARIO,
                 'Co.De.Ma.So': CONSEJERO_DELEGADO_MANCOMUNADO_SOLIDARIO,
                 'Cons.Del.Sol': CONSEJERO_DELEGADO_SOLIDARIO,
                 'SecreNoConsj': SECRETARIO_NO_CONSEJERO,
                 'SECR.NO CONS': SECRETARIO_NO_CONSEJERO,
                 'Scr:no.Cons': SECRETARIO_NO_CONSEJERO,
                 'S.NO CONS.GO': SECRETARIO_NO_CONSEJERO_GO,
                 'MBRO.CONS.GO': MIEMBRO_CONSEJERO_GO,
                 'Auditor': AUDITOR,
                 'Aud.C.Con.': AUDITOR_CUENTAS_CONSOLIDADAS,
                 'AUDT.CTS.CON': AUDITOR_CUENTAS_CONSOLIDADAS,
                 'AUDIT.CC.SUP': AUDITOR_CUENTAS_CONSOLIDADAS_SUPLENTE,
                 'Aud.Supl.': AUDITOR_SUPLENTE,
                 'Auditor Sup.': AUDITOR_SUPLENTE,
                 'AUDITOR SUP.': AUDITOR_SUPLENTE,
                 'Aud.Supl.CC': AUDITOR_SUPLENTE_CUENTAS_CONSOLIDADAS,
                 'Aud.Supl.C.C': AUDITOR_SUPLENTE_CUENTAS_CONSOLIDADAS,
                 'Ent.Reg.Cont': ENT_REG_CONT,
                 'EntidDeposit': ENTIDAD_DEPOSITARIA,
                 'ENT.DEPOSIT.': ENTIDAD_DEPOSITARIA,
                 'Ent.Deposita': ENTIDAD_DEPOSITARIA,
                 'Pte.Comit.Au': PRESIDENTE_COMIT_AUD,
                 'Pte. C. Aud.': PRESIDENTE_COMIT_AUD,
                 'PreComAudit.': PRESIDENTE_COMIT_AUD,
                 'PreComAudit': PRESIDENTE_COMIT_AUD,
                 'Vpres.Com.Au': VICEPRESIDENTE_COMIT_AUD,
                 'Sec.Comit.Au': SECRETARIO_COMIT_AUD,
                 'SecComAudit.': SECRETARIO_COMIT_AUD,
                 'M.Comit.Aud': MIEMBRO_COMIT_AUD,
                 'VocComAudit.': VOCAL_COMIT_AUD,
                 'VocComAudit': VOCAL_COMIT_AUD,
                 'COM.CONTROL': COMISION_CONTROL,
                 'Comis.Contro': COMISION_CONTROL,
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
                 'Vicetes.': VICETESORERO,
                 'VicTesJDirec': VICETESORERO_JUNTA_DIRECTIVA,
                 'Viceteso.J.D': VICETESORERO_JUNTA_DIRECTIVA,
                 'REP.ADM.CONC': REP_ADM_CONC,
                 'Comisario': COMISARIO,
                 'COMISARIO': COMISARIO,
                 'COMISAR.SI.O': COMISARIO_SI_O,
                 'COMISR.SUP.S': COMISARIO_SUP_S,
                 'Gerente': GERENTE,
                 'GERENTE': GERENTE,
                 'Gerente.Adjt': GERENTE_ADJUNTO,
                 'GERENTE SUC.': GERENTE_SUCURSAL,
                 'Gerente Uni.': GERENTE_UNI,
                 'Ger.Eje.': GERENTE_EJECUTIVO,
                 'GERENTE SMCP': GERENTE_SMCP,
                 'Ent. Gestora': ENTIDAD_GESTORA,
                 'Ent.Gestora': ENTIDAD_GESTORA,
                 'ENTI.GESTORA': ENTIDAD_GESTORA,
                 'Ent.Gest.Act': ENTIDAD_GESTORA_ACT,
                 'Ent.Gest.Del': ENTIDAD_GESTORA_DEL,
                 'ENT.GEST.IND': ENTIDAD_GESTORA_INDEPENDIENTE,
                 'ENT.COGESTOR': ENTIDAD_COGESTORA,
                 'Ent.Cogestor': ENTIDAD_COGESTORA,
                 'Auditor Titu': AUDITOR_TITU,
                 'AUDITOR TIT.': AUDITOR_TITU,
                 'AUDIT.CUENT.': AUDITOR_CUENTAS,
                 'Director': DIRECTOR,
                 'DIRECTOR': DIRECTOR,
                 'DTOR.ADMINIS': DIRECTOR_ADMINIS,
                 'Dir.Adm.': DIRECTOR_ADMINIS,
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
                 'DTOR.GEN.FIN': DIRECTOR_GENERAL_FINANCIERO,
                 'DTOR.EJECUT.': DIRECTOR_EJECUTIVO,
                 'DTOR.EXPLOTA': DIRECTOR_EXPLOTA,
                 'DTOR.FABRICA': DIRECTOR_FABRICA,
                 'DTOR.FINANC.': DIRECTOR_FINANCIERO,
                 'DTOR.MARKET.': DIRECTOR_MARKETING,
                 'DTOR.REL.LAB': DIRECTOR_RELACIONES_LABORALES,
                 'DTOR.REC.HUM': DIRECTOR_RECURSOS_HUMANOS,
                 'DTOR.OPERCIO': DIRECTOR_OPERACIONES,
                 'DTOR.SUCURS.': DIRECTOR_SUCURSAL,
                 'DTOR.TECNICO': DIRECTOR_TECNICO,
                 'Dir. Técnico': DIRECTOR_TECNICO,
                 'D. Comercial': DIRECTOR_COMERCIAL,
                 'Dir.Gen.Spl': DIRECTOR_GENERAL_SUPLENTE,
                 'Subdirec': SUBDIRECTOR,
                 'SUBDTOR.GNRL': SUBDIRECTOR_GENERAL,
                 'Subdir.Gral.': SUBDIRECTOR_GENERAL,
                 'Sub.General': SUBDIRECTOR_GENERAL,
                 'ViceDir': VICEDIRECTOR,
                 'Socio': SOCIO,
                 'Socio único': SOCIO_UNICO,
                 'SOCIO COLECT': SOCIO_COLECTIVO,
                 'SocGestor': SOCIO_GESTOR,
                 'SocioGesto': SOCIO_GESTOR,
                 'COMS.DEL.INV': COMS_DEL_INV,
                 'PRE.COMS.D.I': PRESIDENTE_COMS_D_I,
                 'Pte.Com.Inv': PRESIDENTE_COMS_D_I,
                 'M.Comit.Inv': MIEMBRO_COMITE_INV,
                 'MBRO.COM.INV': MIEMBRO_COMITE_INV,
                 'M.Com.Inv': MIEMBRO_COMITE_INV,
                 'PRES.COM.INV': PRESIDENTE_COMISION_INV,
                 'V-PRE.COM.IN': VICEPRESIDENTE_COMISION_INV,
                 'V- PRE.COM.IN': VICEPRESIDENTE_COMISION_INV,
                 'SECR.COM.INV': SECRETARIO_COMISION_INV,
                 'V-SEC.COM.IN': VICESECRETARIO_COMISION_INV,
                 'S.N.C.C.D.I.': S_N_C_C_D_I,
                 'VS.N.C.C.D.I': VS_N_C_C_D_I,
                 'No definido': NO_DEFINIDO,
                 'L. Asesor': LETRADO_ASESOR,
                 'LETRAD.ASES.': LETRADO_ASESOR,
                 'LETRD.ASESOR': LETRADO_ASESOR,
                 'Exp.Ind.': EXP_IND,
                 'COM.LIQ': COMISION_LIQ,
                 'Mmbr.Com.Liq': MIEMBRO_COMISION_LIQ,
                 'MRO.COMS.LIQ': MIEMBRO_COMISION_LIQ,
                 'Miem.Com.Liq': MIEMBRO_COMISION_LIQ,
                 'M.Cons.Liq': MIEMBRO_COMISION_LIQ,
                 'Pres.Com.Liq': PRESIDENTE_COMISION_LIQ,
                 'Pr.Cons.Liq': PRESIDENTE_COMISION_LIQ,
                 'Secr.Com.Liq': SECRETARIO_COMISION_LIQ,
                 'Secr.Cons.Li': SECRETARIO_COMISION_LIQ,
                 'SEC.COMS.LIQ': SECRETARIO_COMISION_LIQ,
                 'Ger.Com.Ger': GER_COMISION_GER,
                 'Miem.Com.Ger': MIEMBRO_COMISION_GER,
                 'MBRO.COM.GER': MIEMBRO_COMISION_GER,
                 'ADMINISTR.': ADMINISTRADOR,
                 'Administrad': ADMINISTRADOR,
                 'ADM.ADJUNTO': ADMINISTRADOR_ADJUNTO,
                 'PRESI.JTA.DI': PRESIDENTE_JUNTA_DIRECTIVA,
                 'Pres.J.Dir.': PRESIDENTE_JUNTA_DIRECTIVA,
                 'PRESID.JUNTA': PRESIDENTE_JUNTA_DIRECTIVA,
                 'V-PRE.JTA.DI': VICEPRESIDENTE_JUNTA_DIRECTIVA,
                 'Vpte.J.Dir.': VICEPRESIDENTE_JUNTA_DIRECTIVA,
                 'V-PR.S.JTA.D': VICEPRESIDENTE_SEGUNDO_JUNTA_DIRECTIVA,
                 'Scrt.J.Dir.': SECRETARIO_JUNTA_DIRECTIVA,
                 'SEC.JTA.DIRE': SECRETARIO_JUNTA_DIRECTIVA,
                 'Vsec.J.Dir.': VICESECRETARIO_JUNTA_DIRECTIVA,
                 'V-SEC.JTA.DI': VICESECRETARIO_JUNTA_DIRECTIVA,
                 'V- SEC.JTA.DI': VICESECRETARIO_JUNTA_DIRECTIVA,
                 'V-SEC.2.JT.D': VICESECRETARIO_SEGUNDO_JUNTA_DIRECTIVA,
                 'Miem.J.Dir.': MIEMBRO_JUNTA_DIRECTIVA,
                 'MBRO.JTA.DIR': MIEMBRO_JUNTA_DIRECTIVA,
                 'VOCAL JTA.DI': VOCAL_JUNTA_DIRECTIVA,
                 'VOC.S.JTA.DI': VOCAL_SECUNDARIO_JUNTA_DIRECTIVA,
                 'TESOR.JTA.DI': TESORERO_JUNTA_DIRECTIVA,
                 'Tes.J.Dir.': TESORERO_JUNTA_DIRECTIVA,
                 'VO.E.P.JT.DI': VOCAL_E_P_JUNTA_DIRECTIVA,
                 'VOC2.JTA.DIR': VOCAL_2_JUNTA_DIRECTIVA,
                 'VOC3.JTA.DIR': VOCAL_3_JUNTA_DIRECTIVA,
                 'VOC4.JTA.DIR': VOCAL_4_JUNTA_DIRECTIVA,
                 'VOC6.JTA.DIR': VOCAL_6_JUNTA_DIRECTIVA,
                 'VOC7.JTA.DIR': VOCAL_7_JUNTA_DIRECTIVA,
                 'VOC10 JTA.DI': VOCAL_10_JUNTA_DIRECTIVA,
                 'CONTAD.JTA.D': CONTAD_JUNTA_DIRECTIVA,
                 'Def.Particip': DEF_PARTICIP,
                 'DEF PARTICIP': DEF_PARTICIP,
                 'Defens.part.': DEF_PARTICIP,
                 'Def.part.': DEF_PARTICIP,
                 'Adm.Judicial': ADM_JUDICIAL,
                 'ADM.JUDICIAL': ADM_JUDICIAL,
                 'Admin.Judic': ADM_JUDICIAL,
                 'Adm.Supl.': ADM_SUPLENTE,
                 'ADM.SUPLENTE': ADM_SUPLENTE,
                 'Com. Audit.': COM_AUDIT,
                 'PreCoAudi': PRESIDENTE_COMISION_AUDIT,
                 'MiCoAudi': MIEMBRO_COMISION_AUDIT,
                 'SEC.COM.AUD.': SECRETARIO_COMISION_AUDIT,
                 'COMIS.AUDITO': COM_AUDIT,
                 'COM.AUD.CTRL': COM_AUDIT_CTRL,
                 'PRE.COM.AUD.': PRESIDENTE_COM_AUD,
                 'PRE.COMS.AUD': PRESIDENTE_COM_AUD,
                 'MBRO.COM.AUD': MIEMBRO_COM_AUD,
                 'REPR.PERMAN.': REPR_PERMAN,
                 'Repr.perman': REPR_PERMAN,
                 'Aud.Su.C.Con': AUDITOR_SU_C_CON,
                 'Pres.J.Rec': PRESIDENTE_JUNTA_RECTORA,
                 'PRE.JTA.RECT': PRESIDENTE_JUNTA_RECTORA,
                 'Vic.Junt.Rec': VICEPRESIDENTE_JUNTA_RECTORA,
                 'Sec.J.Rec': SECRETARIO_JUNTA_RECTORA,
                 'SEC.JTA.RECT': SECRETARIO_JUNTA_RECTORA,
                 'Miem.J.Rec': MIEMBRO_JUNTA_RECTORA,
                 'VOCAL JT.REC': VOCAL_JUNTA_RECTORA,
                 'Miem.Con.Dir': MIEMBRO_CONSEJO_DIRECTIVO,
                 'Pres.Con.Dir': PRESIDENTE_CONSEJO_DIRECTIVO,
                 'Vpre.Con.Dir': VICEPRESIDENTE_CONSEJO_DIRECTIVO,
                 'ComiSinObli': COMI_SIN_OBLI,
                 'M.COM.NOM.RE': MIEMBRO_COMISION_NOM_RE,
                 'Pres.Com.Ej.': PRESIDENTE_COMISION_EJECUTIVA,
                 'PRES.COM.EJE': PRESIDENTE_COMISION_EJECUTIVA,
                 'PRE.COMS.EJE': PRESIDENTE_COMISION_EJECUTIVA,
                 'Pr.Com.Ejecu': PRESIDENTE_COMISION_EJECUTIVA,
                 'Pte.C.Ej': PRESIDENTE_COMISION_EJECUTIVA,
                 'P.Com.Ejec.': PRESIDENTE_COMISION_EJECUTIVA,
                 'Copre.ComEj': COPRESIDENTE_COMISION_EJECUTIVA,
                 'Sec.Com.Ej.': SECRETARIO_COMISION_EJECUTIVA,
                 'Sec.Com.Eje.': SECRETARIO_COMISION_EJECUTIVA,
                 'SEC.COM.EJEC': SECRETARIO_COMISION_EJECUTIVA,
                 'Sec.C.Ej': SECRETARIO_COMISION_EJECUTIVA,
                 'VicSec C.E.': VICESECRETARIO_COMISION_EJECUTIVA,
                 'VicSec.Com.E': VICESECRETARIO_COMISION_EJECUTIVA,
                 'S.NO.C.CO.EJ': SECRETARIO_NO_CONSEJERO_COMISION_EJECUTIVA,
                 'SecrCENoCon': SECRETARIO_COMISION_EJECUTIVA_NO_CONSEJERO,
                 'Vpr.Com.Ejec': VICEPRESIDENTE_COMISION_EJECUTIVA,
                 'Vicpres C.E': VICEPRESIDENTE_COMISION_EJECUTIVA,
                 'Miem.Com.Ej.': MIEMBRO_COMISION_EJECUTIVA,
                 'MRO.COMS.EJE': MIEMBRO_COMISION_EJECUTIVA,
                 'MBRO.COM.EJE': MIEMBRO_COMISION_EJECUTIVA,
                 'M.Com.Ej': MIEMBRO_COMISION_EJECUTIVA,
                 'M.Com.Ejec': MIEMBRO_COMISION_EJECUTIVA,
                 'Com.Ejecutiv': COMISION_EJECUTIVA,
                 'COM.EJECUTIV': COMISION_EJECUTIVA,
                 'Auditor Grup': AUDITOR_GRUP,
                 'PRES.CON.DIR': PRESIDENTE_COMISION_DIRECTIVA,
                 'MiemComDire': MIEMBRO_COMISION_DIRECTIVA,
                 'MiemComDirec': MIEMBRO_COMISION_DIRECTIVA,
                 'MBRO.CON.DIR': MIEMBRO_COMISION_DIRECTIVA,
                 'MBRO.COM.DIR': MIEMBRO_COMISION_DIRECTIVA,
                 'MRO.COMS.DIR': MIEMBRO_COMISION_DIRECTIVA,
                 'SecrComDirec': SECRETARIO_COMISION_DIRECTIVA,
                 'PresComDirec': PRESIDENTE_COMISION_DIRECTIVA,
                 'Vte.Com.Dir.': VICEPRESIDENTE_COMISION_DIRECTIVA,
                 'Suplente': SUPLENTE,
                 'Aud.Manc': AUDITOR_MANCOMUNADO,
                 'Miem.COM.EIC': MIEMBRO_COM_EIC,
                 'Pres.COM.EIC': PRESIDENTE_COM_EIC,
                 'Pdte.Cte.NyR': PRESIDENTE_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES,
                 'PRES.NOMB.RE': PRESIDENTE_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES,
                 'PreComNomRe': PRESIDENTE_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES,
                 'PR.COM.NOM.R': PRESIDENTE_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES,
                 'PR.COMS.NOMB': PRESIDENTE_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES,
                 'Mbro.Cte.NyR': MIEMBRO_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES,
                 'Secr.Cte.NyR': SECRETARIO_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES,
                 'SeCoNoRe': SECRETARIO_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES,
                 'MeCoNoRe': ME_COMITE_NOMBRAMIENTOS_Y_RETRIBUCIONES,
                 'Com.Nomb.': COMISION_NOMB,
                 'Com estrateg': COMISION_ESTRATEG,
                 'MRO.COMS.EST': MIEMBRO_COMISION_ESTRATEG,
                 'R.C.P.SolMan': R_C_P_SOLMAN,
                 'Med.Concusal': MEDIAD_CONCUSAL,
                 'MEDIAD.CONCU': MEDIAD_CONCUSAL,
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
                 'IntervSuspg': INTERVENTOR_SUSPG,
                 'IntervJudic': INTERVENTOR_JUDICIAL,
                 'INTERV.SOLID': INTERVENTOR_SOLIDARIO,
                 'Adm.Sol.Supl': ADMINISTRADOR_SOLIDARIO_SUPLENTE,
                 'PRE.COMS.DEL': PRESIDENTE_COMISION_DELEGADA,
                 'Pres.Com.Del': PRESIDENTE_COMISION_DELEGADA,
                 'SEC.COMS.DEL': SECRETARIO_COMISION_DELEGADA,
                 'Sec.Com.Del': SECRETARIO_COMISION_DELEGADA,
                 'Vsec.Com.Del': VICESECRETARIO_COMISION_DELEGADA,
                 'Con.Del.Com.': CONSEJERO_COMISION_DELEGADA,
                 'Mmbr.Com.Del': MIEMBRO_COMISION_DELEGADA,
                 'MRO.COMS.DEL': MIEMBRO_COMISION_DELEGADA,
                 'Miem.Com.Del': MIEMBRO_COMISION_DELEGADA,
                 'M.Com.Del.No': MIEMBRO_COMISION_DELEGADA,  # "No"?
                 'M.COM.CONSU.': MIEMBRO_COMISION_CONSU,
                 'M.C.Rep.Muni': MIEMBRO_COMISION_REP_MUNI,
                 'Aud.Tit.Grup': AUDITOR_TIT_GRUP,
                 'AUDIT.CONJUN': AUDITOR_CONJUNTO,
                 'Auditor Cons': AUDITOR_CONS,
                 'AUD.C.C.CONJ': AUDITOR_CUENTAS_CONSOLIDADAS_CONJUNTO,
                 'Miem.Com.Rec': MIEMBRO_COMITE_REC,
                 'M.Comit.Rec.': MIEMBRO_COMITE_REC,
                 'M.Supl.Com.R': MIEMBRO_SUPLENTE_COMITE_REC,  # "Miembro suplente"?
                 'Sec.Com.Rec': SECRETARIO_COMITE_REC,
                 'Vsec.Com.Rec': VICESECRETARIO_COMITE_REC,
                 'Delegado': DELEGADO,
                 'DELEGADO': DELEGADO,
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
                 'AdminProvi': ADMINISTRADOR_PROV,
                 'ADM.PROV.SOL': ADMINISTRADOR_PROV_SOLIDARIO,
                 'AdmProvSolEF': ADMINISTRADOR_PROV_SOLIDARIO_EF,
                 'ADJ.GERENCIA': ADJ_GERENCIA,
                 'PRES.HONORI.': PRESIDENTE_HONORIFICO,
                 'Pres. Honor.': PRESIDENTE_HONORIFICO,
                 'Pres.Honorif': PRESIDENTE_HONORIFICO,
                 'V-PRES.HONOR': VICEPRESIDENTE_HONORIFICO,
                 'VicPres.Hono': VICEPRESIDENTE_HONORIFICO,
                 'PreCteAdmres': PRESIDENTE_COMITE_ADM_RES,
                 'Síndico': SINDICO,
                 'SINDICO': SINDICO,
                 'VOCAL': VOCAL,
                 'VOCAL 1': VOCAL_1,
                 'VOCAL 2': VOCAL_2,
                 'VOCAL SUPLEN': VOCAL_SUPLENTE,
                 'MBRO.COM.CTO': MIEMBRO_COM_CTO,
                 'V-P1.COM.CTO': VICEPRESIDENTE_PRIMERO_COM_CTO,
                 'V-P2.COM.CTO': VICEPRESIDENTE_SEGUNDO_COM_CTO,
                 'V-S1.COM.CTO': VICESECRETARIO_PRIMERO_COM_CTO,
                 'V-S2.COM.CTO': VICESECRETARIO_SEGUNDO_COM_CTO,
                 'COMS.ACREED.': COMISION_ACREEDORES,
                 'SUPL.COMS.AC': SUPLENTE_COMISION_ACREEDORES,
                 'Pres.J.Adm': PRESIDENTE_J_ADM,
                 'Pres.J.Adm.': PRESIDENTE_J_ADM,
                 'Vpre.J.Adm.': VICEPRESIDENTE_J_ADM,
                 'Secr.J.Adm.': SECRETARIO_J_ADM,
                 'Teso.J.Adm.': TESORERO_J_ADM,
                 'Miem.J.Adm.': MIEMBRO_J_ADM,
                 'Contador': CONTADOR,
                 'PresComAuCum': PRESIDENTE_COMISION_AU_CUM,
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
                 'PreCoRies': PRESIDENTE_COMISION_RIESGOS,
                 'Pr.Com.Ri.': PRESIDENTE_COMISION_RIESGOS,
                 'V-PRE.COM.RI': VICEPRESIDENTE_COMISION_RIESGOS,
                 'CO.C.RIESGOS': CONSEJERO_COMISION_RIESGOS,
                 'MiCoRies': MIEMBRO_COMISION_RIESGOS,
                 'Miem.Com.Ri.': MIEMBRO_COMISION_RIESGOS,
                 'COMS.VIGILAN': COMS_VIGILAN,
                 'Miem.Com.Acr': MIEMBRO_COMISION_ACREEDORES,
                 'Fundador': FUNDADOR,
                 'SUPL.COMS.CT': SUPLENTE_COMISION_CT,
                 'Miem.C.D.C.A': MIEMBRO_CDCA,
                 'Otorgante': OTORGANTE,
                 'SUPL.COMI.LI': SUPLENTE_COMISION_LIQ,
                 'PRESEN.CONC.': PRESEN_CONC,
                 'COMS.SEGUIM.': COMISION_SEGUIMIENTO,
                 'Pres.COM.SEG': PRESIDENTE_COMISION_SEGUIMIENTO,
                 'Miem.COM.SEG': MIEMBRO_COMISION_SEGUIMIENTO,
                 'AUX.ADM.CONC': AUX_ADMINISTRADOR_CONC,
                 'M.C.Com.Perm': MIEMBRO_C_COMISION_PERM,
                 'MANDATARIO': MANDATARIO,
                 'ENT.ENC.GEST': ENTIDAD_ENC_GESTORA,
                 'COM.CTRL.Y.S': COMISION_CONTROL_Y_S,
                 'PRES.ASAM.SO': PRESIDENTE_ASAM_SO,
                 'MiemComMix': MIEMBRO_COMISION_MIX,
                 'GESTOR': GESTOR,
                 'ENTD.PROMO.': ENTIDAD_PROMOTORA,
                 'ENTI.PROMOT.': ENTIDAD_PROMOTORA,
                 'Censor Cuent': CENSOR_CUENT,
                 'SOC.GEST.ACT': SOCIO_GEST_ACT,
                 'SOCIO HONOR': SOCIO_HONORIFICO,
                 'OBSER.CON.AD': OBSER_CON_AD,
                 'MBRO.COMISIO': MIEMBRO_COMISION,
                 'MiemComIndp': MIEMBRO_COMISION_INDEPENDIENTE,
                 'Sec.G.C.A': SECRETARIO_GCA,
                 'Pres.Junta': PRESIDENTE_JUNTA,
                 'Secr.Junta': SECRETARIO_JUNTA,
                 'Miemb.Cte.CF': MIEMBRO_COMITE_CF,
                 'SUPL.CJO.ADM': SUPLENTE_CONSEJO_ADMINISTRACION,
                 'PresComiGest': PRESIDENTE_COMISION_GESTORA,
                 'Mi.o.c.c': MI_O_C_C,
                 'M.Com. Aseso': MIEMBRO_COM_ASESO,
                 'MBRO.COM.ASE': MIEMBRO_COM_ASESO,
                 'Pre.Com.ANR': PRESIDENTE_COMISION_ANR,
                 'COM.CONS.FAM': COM_CONS_FAM,
                 'M.Com.Seg.Fo': MIEMBRO_COMISION_SEG_FO,
                 'COM.GERENCIA': COM_GERENCIA,
                 'MBRO.C.RESPO': MIEMBRO_COMISION_RESPO,
                 'PTE.COMI.RES': PRESIDENTE_COMISION_RESPO,

                 # hack
                 'Sociedades beneficiarias': SOCIEDADES_BENEFICIARIAS,
                 'Sociedades fusionadas': SOCIEDADES_FUSIONADAS,
                 }
    KEYWORDS = list(_keywords.keys())

    @staticmethod
    def from_string(string):
        try:
            return CARGO._keywords[string]
        except KeyError:
            raise BormeInvalidCargoException(string)
