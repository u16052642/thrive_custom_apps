# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
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
#############################################################################
from thrive import fields, models


class ResConfigSettings(models.TransientModel):
    """Inherit the model res.config.settings to add Additional fields"""
    _inherit = 'res.config.settings'

    is_extra = fields.Boolean(string='Apply Extra Amount',
                              config_parameter='venue_booking_management.is_extra',
                              help="Enable, if extra charge want to add")
    extra_amount = fields.Float(string='Extra Amount',
                                config_parameter='venue_booking_management.extra_amount',
                                help='Enter extra amount/KM')
