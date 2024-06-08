# -*- coding: utf-8 -*-
################################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Gayathri V (info@thrivebureau.com)
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
################################################################################
{
    'name': 'Advanced Cash Flow Statements',
    'version': '17.0.1.0.0',
    'summary': """Generate four levels of cash flow statement reports in PDF and
     Excel""",
    'description': """Generate four levels of cash flow statement reports in PDF 
    and Excel, pdf report, excel report, 
    cashflow, thrive17""",
    'author': "Thrive Bureau Solutions",
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': "https://www.thrivebureau.com",
    'category': 'Accounting',
    'depends': ['base', 'account'],
    'data': ['security/ir.model.access.csv',
             'report/account_wizard_reports.xml',
             'report/account_wizard_templates.xml',
             'views/account_wizard_views.xml',
             ],
    'assets': {
        'web.assets_backend': [
            'advance_cash_flow_statements/static/src/js/action_manager.js'
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
