# # -*- coding: utf-8 -*-

from odoo import models, fields, api

class Organizer(models.Model):
    _name = 'organizer'
    _rec_name = "first_name"
 
    last_name = fields.Char(string="Last Name")
    first_name = fields.Char(string="First Name")
    phone = fields.Char(string="Phone")
    mail = fields.Char(string="Mail")
    gender = fields.Selection([('mr', 'Mr'),('msr', 'Msr')],)
    event_id = fields.Many2one("event.event" , ondelete='cascade' ,string="Event" ,required=True)
    card_state = fields.Selection([('posted','Posted'),('expired','Expired')], 'State', default='posted' ,)