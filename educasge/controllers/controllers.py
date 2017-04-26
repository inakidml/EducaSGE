# -*- coding: utf-8 -*-
from odoo import http

# class Educasge(http.Controller):
#     @http.route('/educasge/educasge/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/educasge/educasge/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('educasge.listing', {
#             'root': '/educasge/educasge',
#             'objects': http.request.env['educasge.educasge'].search([]),
#         })

#     @http.route('/educasge/educasge/objects/<model("educasge.educasge"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('educasge.object', {
#             'object': obj
#         })