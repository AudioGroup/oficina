# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE


from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError



from werkzeug.urls import url_encode

class AccountMoveInherit(models.Model):
    _inherit = "account.move"

    x_delivery_address_sale_order = fields.Char(compute='_compute_x_delivery_address_sale_order')

    @api.depends('x_delivery_address_sale_order')
    def _compute_x_delivery_address_sale_order(self):
        for inv in self:
            order = inv.env['sale.order'].search([('invoice_ids', '=', inv.id)])
            inv.x_delivery_address_sale_order = order.x_delivery_address