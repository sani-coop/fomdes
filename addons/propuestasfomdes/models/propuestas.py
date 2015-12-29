# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Propuestas(models.Model):
    _name = 'propuestasfomdes.propuestas'

    _rec_name = 'codigo_propuesta'

    solicitantes_id = fields.Many2one('propuestasfomdes.solicitantes', string="Solicitante", required=True)

    codigo_propuesta = fields.Char(string="Codigo")

    unidades_productivas_id = fields.Many2one('propuestasfomdes.unidades_productivas', string="Unidad Productiva")
    actividades_productivas_id = fields.Many2one('propuestasfomdes.actividades_productivas', string="Actividad Productiva")

    referencias_solicitante_ids = fields.One2many('propuestasfomdes.referencias_solicitante', 'propuestas_id', string="Referencias del Solicitante")
    garantias_ids = fields.One2many('propuestasfomdes.garantias', 'propuestas_id', string="Garantías")
    avalistas_ids = fields.One2many('propuestasfomdes.avalistas', 'propuestas_id', string="Avalista")
    #referencias_avalista_ids = fields.One2many('propuestasfomdes.referencias_avalista', 'propuestas_id', string='Referencias del Avalista')
    inversiones_ids = fields.One2many('propuestasfomdes.inversiones', 'propuestas_id', string='Plan de Inversiones')

    inversion_total = fields.Float(string='Inversión Total') #calculado!!!
    aporte_propio = fields.Float(string='Aporte Propio') #calculado!!!
    consigno_facturas = fields.Boolean(string='Consignación de Facturas?')
    observaciones = fields.Text(string='Observaciones')

    cedula_solicitante = fields.Char(string='Cédula de Identidad', related='solicitantes_id.cedula', readonly=True)