# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CardRequest(models.Model):
    _name = 'card_request'
    _description = 'Card Create Request'
    _rec_name = 'request_number'
    
    request_number =fields.Char(string='Request Number', required=True, copy=False, readonly=True, default=lambda self: ('New'))
    name = fields.Char(string='Name', required=True, copy=False)
    company_currency = fields.Many2one("res.currency", string='Currency', default=2)
    card_balance = fields.Monetary('Card Balance', digits =(7,2) , currency_field='company_currency', tracking=True, default="1")
    request_data = fields.Date( string='Request Data', default=fields.Date.today)
    request_status = fields.Selection([('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], 'State', default='pending')
    document_ids = fields.Many2many('ir.attachment', string='Documents')
    
    @api.model
    def create(self, vals):
        if vals.get('request_number', ('New')) == ('New'):
            vals['request_number'] =self.env['ir.sequence'].next_by_code('request.number')or  ('New')   
        result = super(CardRequest, self).create(vals)
        return result
  
    def make_approved_it(self):
        self.request_status = 'approved'
     
    def make_rejected_it(self):
        self.request_status = 'rejected'
        