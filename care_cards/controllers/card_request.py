# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
class CreateRequest(http.Controller):
    @http.route('/cards_requests/new' , auth='user', type='http', website=True)
    def new(self, **kw):
        return request.render('care_cards.template_web')
    
    @http.route('/create_cards/create', auth='user', type='http', csrf=False, website=True)
    def create(self, **kw):
 
      request.env['card_request'].sudo().create(kw)
      return request.render('care_cards.patient_thanks')