# -*- coding: utf-8 -*-

from odoo import models, fields, api
class CareCard(models.Model):
    _name = 'card'
    _description = 'Care Card'
    _rec_name = 'card_number'

    card_number = fields.Char('Card Number', required=True, copy=False, readonly=True,  default=lambda self: ('New'))
    beneficiary = fields.Many2one('res.partner', default=lambda self:self.env.user.partner_id.id)
    # beneficiary = fields.Char()
    name = fields.Char('Full Name',)
    expired_date= fields.Date("Expired Date",default=fields.Date.context_today)
    card_date = fields.Date('Card Issue Date', default=fields.Date.today)
    note = fields.Text()
    status = fields.Selection([('activated','Activated'),('expired', 'Expired'),('canceled','Canceled')], 'State', default='activated') 
    company_currency = fields.Many2one("res.currency", string='Currency', default=2, )
    card_balance = fields.Monetary('Card Balance', digits =(7,2), currency_field='company_currency', tracking=True, default="100")
    
    def _date_expiry(self):
        today = fields.Date.today()
        expiry = self.env['card'].search([])
        for order in expiry:
            if order.status == 'activated' and order.expired_date < today:
                order.status = 'expired'

    @api.model
    def create(self, vals):
        vals['card_number'] =self.env['ir.sequence'].next_by_code('card.number')   
        return super(CareCard, self).create(vals)
   
    def activated_it(self):
        self.status = 'activated'
 
    def canceled_it(self):
        self.status = 'canceled'
         