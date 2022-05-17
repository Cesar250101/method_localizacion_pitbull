# -*- coding: utf-8 -*-

from operator import truth

from numpy import True_
from odoo import models, fields, api


class NotasVenta(models.Model):
    _inherit = 'sale.order'
    
    notas_guia = fields.Text(string='Notas Guia Despacho',help='Este texto pasara al campo NOTAS de la guía de despacho')
    crm_producto=fields.Char(string='Producto CMR')
    crm_medio=fields.Char(string='Medio CMR')
    
    
    @api.multi
    def action_confirm(self):
        super(NotasVenta, self).action_confirm()
        if self.notas_guia:
            guia=self.env['stock.picking'].search([('sale_id','=',self.id)],limit=1)
            guia.note=self.notas_guia

    @api.model
    def actualizar_datos_crm(self):
        self.crm_producto=self.opportunity_id.x_producto
        self.crm_medio=self.opportunity_id.x_medio
        return True

        