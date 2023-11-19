# -*- coding: utf-8 -*-

from odoo import models, fields, api


class poolplayer(models.Model):
    _name = 'poolplayer.poolplayer'
    _description = 'poolplayer.poolplayer'

    name = fields.Char()
    dob = fields.Date('Date of Birth')
    gender = fields.Selection([
      ('m', 'Male'),
      ('f', 'Female'),
    ])
    country=fields.Char()
    strongHand = fields.Selection(string='Strong Hand',selection=[
      ('l', 'Left-handed'),
      ('r', 'Right-handed'),
    ])
    img = fields.Image('Image', max_width=256, max_height=256)
    description = fields.Text()


