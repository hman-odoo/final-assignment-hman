# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class Dock(models.Model):
    _name = "dock"
    _description = "Many2one model with stock_transport"

    name = fields.Char(string="Name")
