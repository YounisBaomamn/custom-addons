
from odoo import models, fields, api

class UpdateCardRequest(models.Model):
    _name = 'update_request'
    _rec_name = 'request_number'
    
    card_number = fields.Many2one('care_card',string= 'Card Number')
    request_number =fields.Char(string='Request Number', required=True, copy=False, readonly=True, default=lambda self: ('New'))
    request_data = fields.Date( string='Request Data', default=fields.Date.today)
    request_status = fields.Selection([('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], 'State',default='pending')
    request_type = fields.Selection([('activated','Activated'),('canceled','Canceled')], tring='Request Type', compute='_compute_request_type', store=True)
    document_ids = fields.Many2many('ir.attachment', string="Documents")
    
    @api.model
    def create(self, vals):
        vals['request_number'] =self.env['ir.sequence'].next_by_code('update.request.number')   
        result = super(UpdateCardRequest, self).create(vals)
        return result
    def approved_it(self):
        self.request_status = 'approved'
        self.card_number.write(({'status': self.request_type}))
        
    def rejected_it(self):
        self.request_status = 'rejected'  
        
    @api.onchange('card_number')
    def _onchange_student_ids(self):
        self.request_type = 'canceled' if self.card_number.status == 'activated' else 'activated'

    @api.depends('card_number')
    def _compute_request_type(self):
     for request in self:
      request.request_type = 'canceled' if request.card_number.status == 'activated' else 'activated'