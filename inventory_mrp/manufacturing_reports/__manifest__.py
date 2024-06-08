# -*- coding: utf-8 -*-
#############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Jumana Haseen (<https://www.thrivebureau.com>)
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
{
    'name': 'Manufacturing Reports',
    'version': '17.0.1.0.0',
    'category': 'Manufacturing',
    'summary': 'PDF & XLS Reports For Manufacturing Module',
    'description': 'PDF & XLS reports for manufacturing module with '
                   'advanced filters.',
    'author': 'Thrive Bureau Solutions',
    'website': "http://www.thrivebureau.com",
    'images': ['static/description/banner.png'],
    'company': 'Thrive Bureau Solutions',
    'depends': ['mrp'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/mrp_report_views.xml',
        'reports/mrp_report_templates.xml',
        'reports/mrp_report_reports.xml',
        'views/mrp_report_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'manufacturing_reports/static/src/js/action_manager.js',
        ]
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
