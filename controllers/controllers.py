# -*- coding: utf-8 -*-
from odoo import http

# class MethodLocalizacionPitbull(http.Controller):
#     @http.route('/method_localizacion_pitbull/method_localizacion_pitbull/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_localizacion_pitbull/method_localizacion_pitbull/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_localizacion_pitbull.listing', {
#             'root': '/method_localizacion_pitbull/method_localizacion_pitbull',
#             'objects': http.request.env['method_localizacion_pitbull.method_localizacion_pitbull'].search([]),
#         })

#     @http.route('/method_localizacion_pitbull/method_localizacion_pitbull/objects/<model("method_localizacion_pitbull.method_localizacion_pitbull"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_localizacion_pitbull.object', {
#             'object': obj
#         })