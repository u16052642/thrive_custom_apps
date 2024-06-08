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
from thrive import api, models


class PackingReportValues(models.AbstractModel):
    """Model for report of employee orientation"""
    _name = 'report.employee_orientation.print_pack_template'
    _description = 'Employee Orientation Print report'

    @api.model
    def _get_report_values(self, docids, data=None):
        """Function execute on report values"""
        lst = []
        empl_obj = self.env['hr.employee'].search(
            [('department_id', '=', data['dept_id'])])
        docs = self.env['hr.employee'].browse(docids)
        for line in empl_obj:
            lst.append({
                'doc_ids': docs.ids,
                'doc_model': 'hr.employee',
                'name': line.name,
                'department_id': line.department_id.name,
                'program_name': data['program_name'],
                'company_name': data['company_name'],
                'date_to': data['date_to'],
                'program_convener': data['program_convener'],
                'duration': data['duration'],
                'hours': data['hours'],
                'minutes': data['minutes'],
            })
        return {
            'data': lst,
        }
