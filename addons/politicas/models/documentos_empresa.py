# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DocumentosEmpresa(models.Model):
    _name = 'politicas.documentos_empresa'

    _rec_name = 'tipo_documento'

    tipo_documento = fields.Char(string='Tipo de Documento')
    habilitado = fields.Boolean(string='Habilitar')
    empresa = fields.Char(string='Empresa')
