# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
class CreateRequest(http.Controller):
    @http.route('/cards_requests/new' , auth='user', type='http', website=True)
    def new(self, **kw):
        return request.render('care_cards.create_care_web')
    
    @http.route('/create_cards/create', auth='user', type='http', csrf=False, website=True)
    def create(self, **kw):
 
      vals_request =  {
        'name': kw.get('name'),
        'email': kw.get('email'),
        'phone': kw.get('mobile'),
        'note': kw.get('note'),
        'card_balance': kw.get('card_balance')
        }
      request.env['card_request'].sudo().create(vals_request)
      return request.redirect('/')
  
    @http.route('/create_cards/show',  type='http', csrf=False, website=True)
    def show_my_care_cards(self,**kw):
        request_value = request.env['card'].sudo().search([('beneficiary', '=', request.env.user.partner_id.id)],order='card_number desc', limit=1) 
        val = {
          'card_number' : request_value.card_number,
          'name' : request_value.name,
          'expired_date' : request_value.expired_date,
          'card_date' : request_value.card_date,
           'card_balance' : request_value.card_balance,
           'status' : request_value.status
           
        }
        return request.render('care_cards.show_my_care',val)