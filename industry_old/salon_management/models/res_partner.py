# -*- coding: utf-8 -*-
################################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#    Copyright (C) 2023-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Mohammed Dilshad Tk (info@thrivebureau.com)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
################################################################################
from thrive import fields, models


class ResPartner(models.Model):
    """Inherits 'res partner' to add field to know whether partner is a salon
        partner"""
    _inherit = 'res.partner'

    partner_salon = fields.Boolean(string="Is a Salon Partner",
                                   help="Field to check is partner a salon "
                                        "partner")
