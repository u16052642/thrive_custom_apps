# -*- coding: utf-8 -*-
#############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author:Anjhana A K(<https://www.thrivebureau.com>)
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
#############################################################################
from thrive import api, models


class SaleOrder(models.Model):
    """
This class extends the Sale Order model to include custom fields and methods.
    """
    _inherit = "sale.order"

    @api.depends('partner_id')
    def _compute_note(self):
        """
        Compute the value of the 'note' field for the current record based
        on the value of the 'partner_id' field. If the country associated
        with the partner has a value for 'sale_terms_condition', use that
        value as the note. Otherwise, call the parent method to compute the
        value.
        """
        terms_and_condition = self.partner_id.country_id.sale_terms_condition
        if terms_and_condition:
            self.note = terms_and_condition
        else:
            res = super()._compute_note()
            return res
