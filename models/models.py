# -*- coding: utf-8 -*-

from operator import truth

from numpy import True_
from odoo import models, fields, api
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Partner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def notificar_cambio_vendedor(self):
        # Configuración del servidor SMTP
        servidor=self.env['ir.mail_server'].search([('smtp_user','=','noreply@method.cl')],limit=1)
        smtp_host = servidor.smtp_host
        smtp_port = servidor.smtp_port
        smtp_username = servidor.smtp_user
        smtp_password = servidor.smtp_pass

        # Crear objeto de mensaje
        mensaje = MIMEMultipart()
        mensaje['From'] = 'Method ERP'
        mensaje['To'] = 'nicolas@pitbull.cl,cesar@method.cl'
        mensaje['Subject'] = 'Cambio de vendedor'

        # Cuerpo del mensaje
        cuerpo_mensaje = """
            Estimado/a Pitbull Sociedad Anonima

            Se ha cambiado el vendedor al contacto """ +  self.name+""" , el nuevo vendedor es """ + self.user_id.name +""".

            Saludos.
        """
        mensaje.attach(MIMEText(cuerpo_mensaje, 'plain'))

        # Establecer conexión segura con el servidor SMTP utilizando SSL/TLS
        smtp = smtplib.SMTP_SSL(smtp_host, smtp_port)

        # Iniciar sesión en el servidor SMTP
        smtp.login(smtp_username, smtp_password)

        # Enviar correo electrónico
        smtp.send_message(mensaje)

        # Cerrar conexión con el servidor SMTP
        smtp.quit()

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

        