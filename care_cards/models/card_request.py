
from odoo import models, fields, api

class CardRequest(models.Model):
    
    _inherit = "update_request"
    _name = 'card_request'
    _description = 'Card Create Request'
    
    name = fields.Char('Full Name')
    email = fields.Char('Email',required=True)
    phone = fields.Char( )
    company_currency = fields.Many2one("res.currency", string='Currency', default=2)
    card_balance = fields.Monetary('Card Balance', digits =(7,2), currency_field='company_currency', tracking=True, default="1")
    note = fields.Text( )

    @api.model
    def create(self, vals):
        vals['request_number'] =self.env['ir.sequence'].next_by_code('request.number')   
        result = super(CardRequest, self).create(vals)
        return result
  
    def approved_it(self):
        self.request_status = 'approved'
        self.card_number.create(
            [
                {
                'beneficiary': self.create_uid.partner_id.id,
                'card_balance': self.card_balance,
                'note': self.note,
                'card_date': self.request_data,
                }
            ]
        )
        template = self.env.ref('care_cards.sending_request_email_template')
        self.env['mail.template'].browse(template.id).send_mail(self.id, force_send=True)