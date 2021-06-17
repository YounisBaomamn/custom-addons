# # -*- coding: utf-8 -*-

from odoo import models, fields, api

class Events(models.Model):
    _inherit = 'event.event'
    
    theme_event = fields.Char(string="Theme Event")
    organizer_ids = fields.One2many('organizer' ,'event_id',string='Organizers')
    event_material_ids = fields.Many2many( string='Event Material', comodel_name='material')
    