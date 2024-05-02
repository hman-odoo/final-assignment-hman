# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock Transport',
    'version': '1.0',
    'depends': ['stock_picking_batch', 'fleet', 'stock_delivery'],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_category_views.xml',
        'views/inventory_batch_transfers_views.xml',
    ],
    'demo': [],
    'application': True,
    'license': 'LGPL-3',
}