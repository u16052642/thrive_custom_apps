# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from thrive import api, fields, models, _
from thrive.exceptions import UserError
from thrive.osv import expression


class SaleOrderTemplateLine(models.Model):
    _inherit = "sale.order.template.line"

    @api.model
    def _product_id_domain(self):
        """ Returns the domain of the products that can be added to the template. """
        domain = super(SaleOrderTemplateLine, self)._product_id_domain()
        
        # Add additional criteria based on use_enrol_order
        if self.sale_order_template_id.use_enrol_order:
            domain = expression.AND([domain, [('fee_product', '=', True)]])

        return domain