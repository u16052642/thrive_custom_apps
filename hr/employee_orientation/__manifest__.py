# -*- coding: utf-8 -*-
#############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Jumana Haseen @cybrosys(info@thrivebureau.com)
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
{
    'name': "Employee Orientation & Training",
    'version': '17.0.1.0.0',
    'category': "Human Resources",
    'summary': """Employee Orientation/Training Program Employee orientation by
    which an employee acquires the necessary skills,knowledge, behaviors.""",
    'description': 'Complete Employee Orientation/Training Program  acquire '
                   'the necessary skills,knowledge, behaviors, and contacts to'
                   ' effectively transition into a new organization.',
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': 'https://www.thrivebureau.com',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/employee_training_data.xml',
        'data/orientation_request_data.xml',
        'data/employee_orientation_data.xml',
        'views/checklist_line_views.xml',
        'views/employee_orientation_views.xml',
        'views/employee_training_views.xml',
        'views/orientation_checklist_views.xml',
        'views/orientation_request_views.xml',
        'report/print_pack_certificates_templates.xml',
        'report/print_pack_certificates_report.xml',
        'wizard/orientation_force_complete_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
