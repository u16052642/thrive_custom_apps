# -*- coding: utf-8 -*-
################################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Thrive Bureau Solutions (info@thrivebureau.com)
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
{
    'name': "Equipment Request & IT Operation",
    'version': "17.0.1.0.0",
    'category': 'Human Resources',
    'description': "This module allows your employees to send requests to "
                   "the Department Manager of Equipment for"
                   "equipment type as equipment requests and equipment "
                   "damage expense reimbursement requests Followed"
                   "by Department manager approval and HR Officer approval "
                   "workflow for equipment request and"
                   "equipment damage request",
    'summary': 'Create Equipment Requests',
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'images': ['static/description/banner.jpg'],
    'website': 'https://www.thrivebureau.com',
    'depends': ['base', 'hr_expense', 'hr', 'stock', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'security/user_groups.xml',
        'views/equipment_request_views.xml',
        'report/equipment_report.xml',
        'report/equipment_report_template.xml',
        'views/menu_action.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
