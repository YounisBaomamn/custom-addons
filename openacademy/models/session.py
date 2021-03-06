# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Session"
    
    
    name = fields.Char(required = True )
    start_date = fields.Date()
    duration = fields.Float(digits =(6,3),help="Duration in days")
    seats = fields.Integer(string="Number of Seats", )