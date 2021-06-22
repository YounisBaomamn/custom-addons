from odoo import http
# from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request
# from datetime import datetime

class CardCreateRequest(http.Controller):
  @http.route('/academyss/new', auth='user', type='http', website=True)
  def new(self, **kw):
    return request.render('academy.academy_template')

  @http.route('/create_cards/create', auth='user', type='http', csrf=False, website=True)
  def create(self, **kw):
 
      request.env['academy.teachers'].sudo().create(kw)
      return request.render('academy.patient_thanks', )






# from odoo import http
# from odoo.http import request
# class Academy(http.Controller):

#      @http.route('/academyss/new', type='http', auth="user", website=True)
#      def new(self, **kw):
#       return request.render('academy.academy_template',{})
         
#      @http.route('/create_cards/create',type='http', auth="user", website=True)
#      def create(self, **kw):
#         print(kw)
      #    request_values = {
      #    'note': kw.get('note'),
      #    'email': kw.get('email'),
      #    'mobile': kw.get('mobile'),
      #    'name': kw.get('name')
      #      }
      #    request.env['card_create_request'].sudo().create(request_values)
      #    request.env['academy.teachers'].sudo().create(kw)
      #    return request.render('academy.patient_thanks', )