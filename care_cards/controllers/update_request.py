from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
class UpdateCareCardRequest(http.Controller):
 
   @http.route('/update_card_request/show', auth='user', type='http', csrf=False, website=True)
   def show(self, **kw):
     user_card = request.env['card'].sudo().search([('beneficiary', '=' ,request.env.user.partner_id.id)],order='card_number desc', limit=1 )
     update_values = request.env['update_request'].sudo().search([('card_number', '=', user_card.id)],order='request_number desc', limit=1) 
     vals = {
      
      'request_number': update_values.request_number,
      'request_type': update_values.request_type,
      'request_status': update_values.request_status,
      'request_data': update_values.request_data,
    }
     return request.render('care_cards.update_request_template',vals)
    
   @http.route('/card_update_request/create', auth='user', type='http', csrf=False, website=True)
   def update_request(self, **kw):
     
    user_card = request.env['card'].sudo().search([('beneficiary', '=', request.env.user.partner_id.id)],order='card_number desc', limit=1)
    values = {
      'card_number': user_card.id,
    }
    update_request = request.env['update_request'].sudo().create(values)
    vals = {
      'request_number': update_request.request_number,
      'request_type': update_request.request_type,
      'request_status': update_request.request_status,
      'request_data': update_request.request_data,
    }
    return request.render('care_cards.update_request_template',vals)