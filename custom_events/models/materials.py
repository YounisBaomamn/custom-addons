
# # -*- coding: utf-8 -*-

from odoo import models, fields, api


class Materials(models.Model):
    _name = 'material'
    
    name = fields.Char(string="Name" )
    materials_type = fields.Selection(string='Materials Type', selection=[('sound_equipment', 'Sound Equipment'),('projection_equipment', 'Projection Equipment')])
   