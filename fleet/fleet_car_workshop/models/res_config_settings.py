# -*- coding: utf-8 -*-
###############################################################################
#
# Thrive Bureaulogies Pvt. Ltd.
#
# Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
# Author: Ayana KP (info@thrivebureau.com)
#
# You can modify it under the terms of the GNU AFFERO
# GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
# You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
# (AGPL v3) along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from thrive import fields, models


class ResConfigSettings(models.TransientModel):
    """Inherit config settings for adding journal field """
    _inherit = 'res.config.settings'

    invoice_journal_id = fields.Many2one('account.journal',
                                         string="Car Workshop Journal",
                                         config_parameter='fleet_car_workshop.invoice_journal_type',
                                         help='Set a journal for workshop')
