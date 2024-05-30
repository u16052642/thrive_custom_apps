# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author:  Mruthul Raj (thrive@cybrosys.com)
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
################################################################################
from thrive import fields, models, _
from thrive.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    invoice_count = fields.Integer(string='Invoices',
                                   compute='_compute_invoice_count',
                                   help='The number of associated invoices for '
                                        'this picking.')
    operation_code = fields.Selection(related='picking_type_id.code',
                                      string='Operation Code',
                                      help='The code related to the operation '
                                           'of this picking.')
    is_return = fields.Boolean(string='Return',
                               help='Indicates whether this picking is a '
                                    'return.')

    def _compute_invoice_count(self):
        """This computes function used to count the number of invoice for
        the picking"""
        for picking_id in self:
            move_ids = picking_id.env['account.move'].search(
                [('transfer_ids', 'in', picking_id.id)])
            if move_ids:
                self.invoice_count = len(move_ids)
            else:
                self.invoice_count = 0

    def action_create_invoice(self):
        """This is the function for creating customer invoice
        from the picking"""
        for picking_id in self:
            current_user = self.env.uid
            if picking_id.picking_type_id.code == 'outgoing':
                customer_journal_id = \
                    picking_id.env['ir.config_parameter'].sudo(). \
                        get_param('stock_move_invoice.customer_journal_id') or \
                    False
                if not customer_journal_id:
                    raise UserError(
                        _("Please configure the journal from settings"))
                invoice_line_list = []
                for move_ids_without_package in picking_id. \
                        move_ids_without_package:
                    vals = (0, 0, {
                        'name': move_ids_without_package.description_picking,
                        'product_id': move_ids_without_package.product_id.id,
                        'price_unit':
                            move_ids_without_package.product_id.lst_price,
                        'account_id':
                            move_ids_without_package.product_id.
                            property_account_income_id.id if
                            move_ids_without_package.
                            product_id.property_account_income_id
                            else move_ids_without_package.
                            product_id.categ_id.
                            property_account_income_categ_id.id,
                        'tax_ids': [(6, 0, [
                            picking_id.company_id.account_sale_tax_id.id])],
                        'quantity': move_ids_without_package.quantity,
                    })
                    invoice_line_list.append(vals)
                    invoice = picking_id.env['account.move'].create({
                        'move_type': 'out_invoice',
                        'invoice_origin': picking_id.name,
                        'invoice_user_id': current_user,
                        'narration': picking_id.name,
                        'partner_id': picking_id.partner_id.id,
                        'currency_id':
                            picking_id.env.user.company_id.currency_id.id,
                        'journal_id': int(customer_journal_id),
                        'payment_reference': picking_id.name,
                        'picking_id': picking_id.id,
                        'invoice_line_ids': invoice_line_list,
                        'transfer_ids': self
                    })
                    return invoice

    def action_create_bill(self):
        """This is the function for creating vendor bill
                from the picking"""
        for picking_id in self:
            current_user = self.env.uid
            if picking_id.picking_type_id.code == 'incoming':
                vendor_journal_id = picking_id.env[
                                        'ir.config_parameter'].sudo().get_param(
                    'stock_move_invoice.vendor_journal_id') or False
                if not vendor_journal_id:
                    raise UserError(
                        _("Please configure the journal from the settings."))
                invoice_line_list = []
                for move_ids_without_package in picking_id. \
                        move_ids_without_package:
                    vals = (0, 0, {
                        'name': move_ids_without_package.description_picking,
                        'product_id': move_ids_without_package.product_id.id,
                        'price_unit':
                            move_ids_without_package.product_id.lst_price,
                        'account_id':
                            move_ids_without_package.product_id.
                            property_account_income_id.id if
                            move_ids_without_package.product_id.
                            property_account_income_id
                            else move_ids_without_package.product_id.categ_id.
                            property_account_income_categ_id.id,
                        'tax_ids': [(6, 0, [
                            picking_id.company_id.account_purchase_tax_id.id])],
                        'quantity': move_ids_without_package.quantity,
                    })
                    invoice_line_list.append(vals)
                    invoice = picking_id.env['account.move'].create({
                        'move_type': 'in_invoice',
                        'invoice_origin': picking_id.name,
                        'invoice_user_id': current_user,
                        'narration': picking_id.name,
                        'partner_id': picking_id.partner_id.id,
                        'currency_id':
                            picking_id.env.user.company_id.currency_id.id,
                        'journal_id': int(vendor_journal_id),
                        'payment_reference': picking_id.name,
                        'picking_id': picking_id.id,
                        'invoice_line_ids': invoice_line_list,
                        'transfer_ids': self
                    })
                    return invoice

    def action_create_customer_credit(self):
        """This is the function for creating customer credit note
                from the picking"""
        for picking_id in self:
            current_user = picking_id.env.uid
            if picking_id.picking_type_id.code == 'incoming':
                customer_journal_id = \
                    picking_id.env['ir.config_parameter'].sudo(). \
                        get_param('stock_move_invoice.customer_journal_id') or \
                    False
                if not customer_journal_id:
                    raise UserError(
                        _("Please configure the journal from settings"))
                invoice_line_list = []
                for move_ids_without_package in picking_id. \
                        move_ids_without_package:
                    vals = (0, 0, {
                        'name': move_ids_without_package.description_picking,
                        'product_id': move_ids_without_package.product_id.id,
                        'price_unit':
                            move_ids_without_package.product_id.lst_price,
                        'account_id': move_ids_without_package.product_id.
                            property_account_income_id.id if
                        move_ids_without_package.product_id.
                            property_account_income_id
                        else move_ids_without_package.product_id.categ_id.
                            property_account_income_categ_id.id,
                        'tax_ids': [(6, 0, [
                            picking_id.company_id.account_sale_tax_id.id])],
                        'quantity': move_ids_without_package.quantity,
                    })
                    invoice_line_list.append(vals)
                    invoice = picking_id.env['account.move'].create({
                        'move_type': 'out_refund',
                        'invoice_origin': picking_id.name,
                        'invoice_user_id': current_user,
                        'narration': picking_id.name,
                        'partner_id': picking_id.partner_id.id,
                        'currency_id':
                            picking_id.env.user.company_id.currency_id.id,
                        'journal_id': int(customer_journal_id),
                        'payment_reference': picking_id.name,
                        'picking_id': picking_id.id,
                        'invoice_line_ids': invoice_line_list,
                        'transfer_ids': self
                    })
                    return invoice

    def action_create_vendor_credit(self):
        """This is the function for creating refund
                from the picking"""
        for picking_id in self:
            current_user = self.env.uid
            if picking_id.picking_type_id.code == 'outgoing':
                vendor_journal_id = picking_id.env[
                                        'ir.config_parameter'].sudo().get_param(
                    'stock_move_invoice.vendor_journal_id') or False
                if not vendor_journal_id:
                    raise UserError(
                        _("Please configure the journal from the settings."))
                invoice_line_list = []
                for move_ids_without_package in picking_id. \
                        move_ids_without_package:
                    vals = (0, 0, {
                        'name': move_ids_without_package.description_picking,
                        'product_id': move_ids_without_package.product_id.id,
                        'price_unit':
                            move_ids_without_package.product_id.lst_price,
                        'account_id': move_ids_without_package.product_id.
                            property_account_income_id.id if
                        move_ids_without_package.product_id.
                            property_account_income_id
                        else move_ids_without_package.product_id.categ_id.
                            property_account_income_categ_id.id,
                        'tax_ids': [(6, 0, [
                            picking_id.company_id.account_purchase_tax_id.id])],
                        'quantity': move_ids_without_package.quantity,
                    })
                    invoice_line_list.append(vals)
                    invoice = picking_id.env['account.move'].create({
                        'move_type': 'in_refund',
                        'invoice_origin': picking_id.name,
                        'invoice_user_id': current_user,
                        'narration': picking_id.name,
                        'partner_id': picking_id.partner_id.id,
                        'currency_id':
                            picking_id.env.user.company_id.currency_id.id,
                        'journal_id': int(vendor_journal_id),
                        'payment_reference': picking_id.name,
                        'picking_id': picking_id.id,
                        'invoice_line_ids': invoice_line_list,
                        'transfer_ids': self
                    })
                    return invoice

    def action_open_picking_invoice(self):
        """This is the function of the smart button which redirect to the
        invoice related to the current picking"""
        return {
            'name': 'Invoices',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'domain': [('transfer_ids', 'in', self.id)],
            'context': {'create': False},
            'target': 'current'
        }

    def action_create_multi_invoice_for_multi_transfer(self):
        """This is the function for creating customer invoice
        from the picking"""
        picking_type = list(self.picking_type_id)
        if all(first == picking_type[0] for first in picking_type):
            if self.picking_type_id.code == 'outgoing':
                partner = list(self.partner_id)
                if all(first == partner[0] for first in partner):
                    partner_id = self.partner_id
                    invoice_line_list = []
                    customer_journal_id = \
                        self.env['ir.config_parameter'].sudo(). \
                            get_param('stock_move_invoice.customer_journal_id') \
                        or False
                    if not customer_journal_id:
                        raise UserError(
                            _("Please configure the journal from settings"))
                    for picking_id in self:
                        for move_ids_without_package in picking_id. \
                                move_ids_without_package:
                            vals = (0, 0, {
                                'name':
                                    move_ids_without_package.description_picking
                                ,
                                'product_id':
                                    move_ids_without_package.product_id.id,
                                'price_unit': move_ids_without_package.
                                    product_id.lst_price,
                                'account_id': move_ids_without_package.
                                    product_id.property_account_income_id.id if
                                move_ids_without_package.product_id.
                                    property_account_income_id
                                else move_ids_without_package.
                                    product_id.categ_id.
                                    property_account_income_categ_id.id,
                                'tax_ids': [(6, 0, [picking_id.company_id.
                                             account_purchase_tax_id.id])],
                                'quantity':
                                    move_ids_without_package.quantity,
                            })
                            invoice_line_list.append(vals)
                    invoice = self.env['account.move'].create({
                        'move_type': 'out_invoice',
                        'invoice_origin': picking_id.name,
                        'invoice_user_id': self.env.uid,
                        'narration': picking_id.name,
                        'partner_id': partner_id.id,
                        'currency_id':
                            picking_id.env.user.company_id.currency_id.id,
                        'journal_id': int(customer_journal_id),
                        'payment_reference': picking_id.name,
                        'invoice_line_ids': invoice_line_list,
                        'transfer_ids': self
                    })
                else:
                    for picking_id in self:
                        picking_id.create_invoice()
            elif self.picking_type_id.code == 'incoming':
                partner = list(self.partner_id)
                if all(first == partner[0] for first in partner):
                    partner_id = self.partner_id
                    bill_line_list = []
                    vendor_journal_id = \
                        self.env['ir.config_parameter'].sudo(). \
                            get_param('stock_move_invoice.vendor_journal_id') \
                        or False
                    if not vendor_journal_id:
                        raise UserError(_("Please configure the journal from "
                                          "the settings."))
                    for picking_id in self:
                        for move_ids_without_package in picking_id. \
                                move_ids_without_package:
                            vals = (0, 0, {
                                'name':
                                    move_ids_without_package.description_picking
                                ,
                                'product_id':
                                    move_ids_without_package.product_id.id,
                                'price_unit': move_ids_without_package.
                                    product_id.lst_price,
                                'account_id': move_ids_without_package.
                                    product_id.property_account_income_id.id if
                                move_ids_without_package.product_id.
                                    property_account_income_id
                                else move_ids_without_package.
                                    product_id.categ_id.
                                    property_account_income_categ_id.id,
                                'tax_ids': [(6, 0, [picking_id.company_id.
                                             account_purchase_tax_id.id])],
                                'quantity':
                                    move_ids_without_package.quantity,
                            })
                            bill_line_list.append(vals)
                    invoice = self.env['account.move'].create({
                        'move_type': 'in_invoice',
                        'invoice_origin': picking_id.name,
                        'invoice_user_id': self.env.uid,
                        'narration': picking_id.name,
                        'partner_id': partner_id.id,
                        'currency_id':
                            picking_id.env.user.company_id.currency_id.id,
                        'journal_id': int(vendor_journal_id),
                        'payment_reference': picking_id.name,
                        'picking_id': picking_id.id,
                        'invoice_line_ids': bill_line_list,
                        'transfer_ids': self
                    })
                else:
                    for picking_id in self:
                        picking_id.create_bill()
        else:
            raise UserError(
                _("Please select single type transfer"))
