# # -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomPartner(models.Model):
    _inherit = 'res.partner'
    
    is_organization = fields.Boolean(string='Is Organization')
    
   