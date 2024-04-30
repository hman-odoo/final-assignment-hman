# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class StockPicking(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(compute="_compute_total_volume", string="Volume")

    @api.depends('product_id.volume', 'move_ids.quantity')
    def _compute_total_volume(self):
        for rec in self:
            for prod in rec:
                list1 = prod.move_ids.mapped('quantity')
                list2 = prod.move_ids.product_id.mapped('volume')
                volume_sum = sum(x * y for x, y in zip(list1, list2))
            rec.volume = volume_sum