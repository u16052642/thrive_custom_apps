# -*- coding: utf-8 -*-
#############################################################################
#    A part of Open HRMS Project <https://www.openhrms.com>
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Thrive Bureau Solutions(<https://www.thrivebureau.com>)
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


class HrContractAdvantageTemplate(models.Model):
    """Create a new model for adding fields."""
    _name = 'hr.contract.advantage.template'
    _description = "Employee's Advantage on Contract"

    name = fields.Char('Name', required=True,
                       help="Name for Employee's Advantage on Contract")
    code = fields.Char('Code', required=True,
                       help="Code for Employee's Advantage on Contract")
    lower_bound = fields.Float('Lower Bound',
                               help="Lower bound authorized by the employer"
                                    "for this advantage")
    upper_bound = fields.Float('Upper Bound',
                               help="Upper bound authorized by the employer"
                                    "for this advantage")
    default_value = fields.Float(string="Default Value",
                                 help='Default value for this advantage')
