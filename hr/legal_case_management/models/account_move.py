# -*- coding: utf-8 -*-
###############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Gayathri V (info@thrivebureau.com)
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
###############################################################################
from thrive import fields, models


class AccountMove(models.Model):
    """Inherit account move"""
    _inherit = 'account.move'

    case_ref = fields.Char(readonly=True, string='Case Reference',
                           help='It is used to identify the case reference')
