# -*- coding: utf-8 -*-

from odoo import models, fields, api


class estate(models.Model):
    _name = 'estate.estate'
    _description = 'estate.estate'

    name = fields.Char(required=True, default="Unknown")
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date()
    expected_price=fields.Float(required=True)
    selling_price=fields.Float()
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection(
      string='Garden Orientation',
      selection=[
      ('north','North'),
      ('south','South'),
      ('east','East'),
      ('west','West'),
    ])
    active=fields.Boolean()


