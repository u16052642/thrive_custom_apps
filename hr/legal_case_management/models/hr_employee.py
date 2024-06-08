# -*- coding: utf-8 -*-
###############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Gayathri V(info@thrivebureau.com)
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


class HrEmployee(models.Model):
    """To create lawyers"""
    _inherit = 'hr.employee'

    is_lawyer = fields.Boolean(string="Is Lawyer",
                               help='Is this employee is a lawyer')
    wage_per_trial = fields.Integer(string="Wage Per Trial",
                                    help='Wage per trial')
    wage_per_case = fields.Integer(string="Wage Per Case", help='Wage per Case')
    not_available = fields.Boolean(string='Not Available',
                                   help='Lawyer Unavailable')
