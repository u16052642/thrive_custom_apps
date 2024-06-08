# -*- coding: utf-8 -*-
##############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Saneen K (info@thrivebureau.com)
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
##############################################################################
from thrive import api, models


class MrpBom(models.Model):
    """ This class extends the standard MRP Bill of Materials (BOM) model
     to incorporate changes related to variants."""
    _inherit = 'mrp.bom'

    @api.onchange("product_tmpl_id")
    def _onchange_product_tmpl_id(self):
        """ This method updates the product ID based on the selected
        product template ID."""
        self.product_id = self.env['product.product'].search(
            [('product_tmpl_id', '=', self.product_tmpl_id.id)])
