# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pool_Player(models.Model):
    _name = 'pool_player'
    _description = 'Pool Player'

    name = fields.Char()
    dob = fields.Date()
    gender=field_name = fields.Selection([
      ('key', 'value')
    ], string='field_name')
    field_name = fields.Date('field_name')
    field_name = fields.Char('field_name')

    description = fields.Text()

    # value2 = fields.Float(compute="_value_pc", store=True)
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
