# -*- coding: utf-8 -*-
#############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
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
{
    'name': 'Hide Create|Delete|Archive|Export Options - Model Wise',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools, Productivity',
    'summary': """ Can hide options from user """,
    'description': """ By using this module we can hide the options like create,
    delete,export,and archive/un archive in the model which we want. Here we
     are also able to select the user groups except Administrator which we want 
     to apply the above hiding functionality """,
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': "https://www.thrivebureau.com",
    'depends': ['base_setup', 'mail','web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/access_right_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'model_access_rights//static/src/**/*',
        ]
    },
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
