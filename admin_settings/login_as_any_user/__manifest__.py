# -*- coding: utf-8 -*-
###############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Sabeel B (info@thrivebureau.com)
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
{
    'name': 'Login As Any User',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Admin can log in as any user',
    'description': 'The "Login As Any User" module allows administrators to '
                   'switch to any user account without the need for '
                   'passwords or other authentication.',
    'author': 'Thrive Bureau Solution',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solution',
    'website': 'https://www.thrivebureau.com',
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'wizards/user_selection_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'login_as_any_user/static/src/js/systray_button.js',
            'login_as_any_user/static/src/xml/systray_button_templates.xml',
        ]},
    'images': [
        'static/description/banner.jpg'
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto-install': False,
    'application': False,
}
