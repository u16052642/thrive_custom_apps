# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions (thrive@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from thrive import api, fields, models, _
from thrive.exceptions import ValidationError


class SaleOrder(models.Model):
    """Inherit the 'sale_order' model to confirm Sale Orders, Create Invoices,
    Validate Invoices, and Print Bills when 'Confirm Quotation',
    'Create Invoice', 'Validate Invoice', and 'Print Invoices'
    are enabled in Configuration Settings."""
    _inherit = 'sale.order'

    automate_print_invoices = fields.Boolean(
        string='Print Invoices',
        help="Print invoices for corresponding purchase orders")

    @api.model_create_multi
    def create(self, vals_list):
        """
            Super the method create to confirm quotation, create and validate
            invoice
        """
        res = super(SaleOrder, self).create(vals_list)
        automate_purchase = self.env['ir.config_parameter'].sudo().get_param(
            'automate_sale')
        automate_invoice = self.env['ir.config_parameter'].sudo().get_param(
            'automate_invoice')
        automate_print_invoices = self.env[
            'ir.config_parameter'].sudo().get_param('automate_print_invoices')
        automate_validate_invoice = self.env[
            'ir.config_parameter'].sudo().get_param('automate_validate_invoice')
        if automate_print_invoices:
            res.automate_print_invoices = True
        if automate_purchase:
            res.action_confirm()
            if automate_invoice:
                for rec in vals_list[0].get('order_line'):
                    product = self.env['product.template'].search(
                        [('id', '=', rec[2].get('product_template_id'))])
                    if product.invoice_policy == 'delivery':
                        raise ValidationError(
                            _("Please choose only ordered invoicing policy"))
                    else:
                        res._create_invoices()
                if automate_validate_invoice:
                    res.invoice_ids.action_post()
        return res

    def action_print_invoice(self):
        """Method to print invoice"""
        return self.env.ref('account.account_invoices').report_action(
            self.invoice_ids)
