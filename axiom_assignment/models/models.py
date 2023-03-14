# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class axiom_assignment(models.Model):
#     _name = 'axiom_assignment.axiom_assignment'
#     _description = 'axiom_assignment.axiom_assignment'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
