# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE


from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError



from werkzeug.urls import url_encode


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    x_delivery_address = fields.Char(string="Dirección de entrega")