# -*- coding: utf-8 -*-
# from odoo import http


# class Myevents(http.Controller):
#     @http.route('/myevents/myevents/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myevents/myevents/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myevents.listing', {
#             'root': '/myevents/myevents',
#             'objects': http.request.env['myevents.myevents'].search([]),
#         })

#     @http.route('/myevents/myevents/objects/<model("myevents.myevents"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myevents.object', {
#             'object': obj
#         })
