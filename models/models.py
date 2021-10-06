# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NotasVenta(models.Model):
    _inherit = 'sale.order'
    
    notas_guia = fields.Text(string='Notas Guia Despacho',help='Este texto pasara al campo NOTAS de la guía de despacho')
    
    
    @api.multi
    def action_confirm(self):
        if self.notas_guia:
            super(NotasVenta, self).action_confirm()
            guia=self.env['stock.picking'].search([('sale_id','=',self.id)],limit=1)
            guia.note=self.notas_guia
        