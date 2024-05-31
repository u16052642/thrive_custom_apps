# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2024 ZestyBeanz Technologies(<http://www.zbeanztech.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Employee Documents Expiry Management',
    'version': '17.0.0.1',
    'summary': 'This module allows adding employee-related documents and provides expiry alerts via email and a dashboard view.',
    'category':'Hr',
    'website': 'http://www.zbeanztech.com/',
    'description': """
            This module allows adding employee-related documents and provides expiry alerts via email and a dashboard view.
    """,
    'author': 'ZestyBeanz Technologies',
    'maintainer': 'ZestyBeanz Technologies',
    'support': 'support@zbeanztech.com',
    'license': 'LGPL-3',
    'icon': "/zb_employee_documents_management/static/description/icon.png",
    'images': ['static/description/banners/banner.gif',],
    'currency': 'USD',
    'price': 0.0,
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/document_expiry_mail.xml',
        'data/document_expiry_scheduler.xml',
        'views/res_config_settings_view.xml',
        'views/hr_employee_views.xml',
        'views/employee_documents_views.xml',
        
        ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}