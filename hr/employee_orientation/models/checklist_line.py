# -*- coding: utf-8 -*-
#############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Jumana Haseen @cybrosys(info@thrivebureau.com)
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
#############################################################################
from thrive import models, fields


class ChecklistLine(models.Model):
    """This class creates a model 'checklist.line' and adds required fields """
    _name = 'checklist.line'
    _description = 'Checklist Line'
    _rec_name = 'line_name'

    line_name = fields.Char(string='Name', required=True,
                            help="Checklist name.")
    responsible_user_id = fields.Many2one('res.users',
                                          string='Responsible User',
                                          required=True,
                                          help="Give the responsible user.")
