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
from thrive import fields, models


class AccountMove(models.Model):
    """Inheriting the model account.move"""
    _inherit = 'account.move'

    picking_id = fields.Many2one('stock.picking', string='Picking',
                                 help='Related picking for this accounting '
                                      'entry')
    transfer_ids = fields.Many2many('stock.picking', string='Transfers',
                                    help='Related transfers for this accounting'
                                         ' entry')
