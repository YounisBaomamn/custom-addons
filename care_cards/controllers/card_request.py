# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
class CreateRequest(http.Controller):
    @http.route('/cards_requests/new' , auth='user', type='http', website=True)
    def new(self, **kw):
        return request.render('care_cards.template_web')
    
    @http.route('/create_cards/create', auth='user', type='http', csrf=False, website=True)
    def create(self, **kw):
 
      request.env['card_request'].sudo().create(kw)
      return request.render('care_cards.patient_thanks')
  
    @http.route('/create_cards/show',  type='http', csrf=False, website=True)
    def show_my_care_cards(self,**kw):
        value = request.env['card'].sudo().search([]) 
        return request.render('care_cards.show_my_care',{'value':value})