# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.exceptions import ValidationError

class InventoryBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one('dock', string="Dock")
    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle")
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category',string="Vehicle Category")
    weight = fields.Float(string="Weight", compute="_compute_total_weight", store=True)
    weight_perc = fields.Float(compute="_compute_percentage")
    volume = fields.Float(string="Volume", compute="_compute_total_volume", store=True)
    volume_perc = fields.Float(compute="_compute_percentage")
    no_of_transfers = fields.Integer(compute="_compute_no_of_transfers", store=True)
    no_of_lines = fields.Integer(compute="_compute_no_of_lines", store=True)
    driver_id = fields.Many2one(related='vehicle_id.driver_id', store=True)

    @api.constrains('volume')
    def _check_volume_perc(self):
        for rec in self:
            if rec.volume > rec.vehicle_category_id.max_volume:
                raise ValidationError('Volume precentage cannot be greater than 100%')

    @api.depends('picking_ids.volume')
    def _compute_total_volume(self):
        for rec in self:
            rec.volume = sum(rec.picking_ids.mapped('volume'))
            
    @api.depends('picking_ids.shipping_weight')
    def _compute_total_weight(self):
        for rec in self:
            rec.weight = sum(rec.picking_ids.mapped('shipping_weight'))

    @api.depends('weight','volume')
    def _compute_percentage(self):
        for rec in self:
            if rec.vehicle_category_id.max_weight :
                rec.weight_perc = (rec.weight/rec.vehicle_category_id.max_weight)*100
            else:
                rec.weight_perc = 0

            if rec.vehicle_category_id.max_volume :
                rec.volume_perc = (rec.volume/rec.vehicle_category_id.max_volume)*100
            else:
                rec.volume_perc = 0

    @api.depends('picking_ids')
    def _compute_no_of_transfers(self):
        for rec in self:
            rec.no_of_transfers = len(rec.picking_ids)

    @api.depends('move_line_ids')
    def _compute_no_of_lines(self):
        for rec in self:
            rec.no_of_lines = len(rec.move_line_ids)