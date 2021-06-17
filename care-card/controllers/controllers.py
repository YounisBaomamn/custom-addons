# -*- coding: utf-8 -*-
# from odoo import http


# class CareCard(http.Controller):
#     @http.route('/care_card/care_card/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/care_card/care_card/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('care_card.listing', {
#             'root': '/care_card/care_card',
#             'objects': http.request.env['care_card.care_card'].search([]),
#         })

#     @http.route('/care_card/care_card/objects/<model("care_card.care_card"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('care_card.object', {
#             'object': obj
#         })
