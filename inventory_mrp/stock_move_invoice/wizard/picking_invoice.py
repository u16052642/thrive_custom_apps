# -*- coding: utf-8 -*-
################################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author:  Mruthul Raj (info@thrivebureau.com)
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
from thrive import models


class PickingInvoice(models.TransientModel):
    """model for picking invoice wizard"""
    _name = 'picking.invoice'
    _description = "Picking Invoice"

    def action_picking_multi_invoice(self):
        """Function to create multiple invoice for multiple
        picking from wizard"""
        active_ids = self._context.get('active_ids')
        picking_ids = self.env['stock.picking'].browse(active_ids)
        picking_id = picking_ids.filtered(
            lambda x: x.state == 'done' and x.invoice_count == 0)
        for picking in picking_id:
            if picking.picking_type_id.code == 'incoming' and not picking.is_return:
                picking.create_bill()
            if picking.picking_type_id.code == 'outgoing' and not picking.is_return:
                picking.create_invoice()
            if picking.picking_type_id.code == 'incoming' and picking.is_return:
                picking.create_vendor_credit()
            if picking.picking_type_id.code == 'outgoing' and picking.is_return:
                picking.create_customer_credit()
