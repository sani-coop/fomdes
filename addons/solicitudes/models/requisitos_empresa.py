# -*- coding: utf-8 -*-

from openerp import models, fields, api

class RequisitosEmpresa(models.Model):
    _name = 'solicitudes.requisitos_empresa'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Número de expediente")
    documentos_empresa_id = fields.Many2one('politicas.documentos_empresa', string="Tipo de Documento")
    documento = fields.Char(string='Documento')
    observaciones = fields.Char(string='Observaciones')
    valido = fields.Boolean(string='Valido')

    empresa_establecida_solicitud = fields.Boolean(string='Empresa establecida?', related='solicitudes_id.empresa_establecida', readonly=True)
