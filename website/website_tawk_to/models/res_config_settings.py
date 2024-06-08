# -*- coding: utf-8 -*-
###############################################################################
#
#  Thrive Bureaulogies Pvt. Ltd.
#
#  Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#  Author: Ranjith R (info@thrivebureau.com)
#
#  You can modify it under the terms of the GNU LESSER
#  GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#  You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#  (LGPL v3) along with this program.
#  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from thrive import fields, models


class ResConfigSettings(models.TransientModel):
    """This model is to add an property_id and widget_id in the settings"""
    _inherit = "res.config.settings"

    property_id = fields.Char(string="Property ID",
                              config_parameter='website_tawk_to.property_id',
                              help="Please enter the property id of tawk to.")
    widget_id = fields.Char(string="Widget ID",
                            config_parameter='website_tawk_to.widget_id',
                            help="Please enter the website id of tawk to.")
