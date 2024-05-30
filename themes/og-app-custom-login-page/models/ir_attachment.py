# -*- coding: utf-8 -*-
################################################################################
#
#    Ogroni Informatix Limited
#
#    Copyright (C) 2024-TODAY Ogroni Informatix Limited(<https://www.ogroni.com/>).
#    Author: Billal (billal.hossain@ogroni.com)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

from thrive import fields, models


class IrAttachment(models.Model):
    """Inherit 'ir.attachment' to add is_background field"""
    _inherit = 'ir.attachment'

    is_background = fields.Boolean(string="Is Background", default=False,
                                   help="To check is background option added")
