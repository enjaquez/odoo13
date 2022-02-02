# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Sale_field(models.Model):

    _inherit='account.move'

    aref = fields.Reference([('sale_order', 'String')])
    x_orden_de_compra = fields.Char(string='Orden de Compra', compute="_orden_agregar")

    #@api.multi
    #@api.depends('origin')
    def _orden_agregar(self):
        for record in self:
             record['x_orden_de_compra'] = self.env['sale.order'].search([('name', '=', self.invoice_origin)]).x_studio_orden_de_compra




