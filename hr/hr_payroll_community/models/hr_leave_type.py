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


class HrLeaveType(models.Model):
    """Inherit hr_leave_type for adding code."""
    _inherit = "hr.leave.type"
    _description = "Time Off Type"

    code = fields.Char(string="Code", help="Code for Time Off Type")
