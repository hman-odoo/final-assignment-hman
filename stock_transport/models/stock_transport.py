# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class StockTransport(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float(string="Max Weight(Kg)")
    max_volume = fields.Float(string="Max Volume(m³)")

    @api.depends('max_weight', 'max_volume')
    def _compute_display_name(self):
        for category in self:
            category.display_name = f"{category.name} ({category.max_weight}kg, {category.max_volume}m³)"
