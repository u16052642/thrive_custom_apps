# -*- coding: utf-8 -*-
###############################################################################
#
#   Thrive Bureaulogies Pvt. Ltd.
#
#   Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#   Author: Jumana Haseen ( info@thrivebureau.com )
#
#   You can modify it under the terms of the GNU AFFERO
#   GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#   You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#   (AGPL v3) along with this program.
#   If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': "Onedrive Integration",
    'version': "17.0.1.0.0",
    'category': "Productivity",
    'summary': """Upload and download files in Onedrive using thrive """,
    'description': """This module was developed to upload files to Onedrive as 
    well as access files from Onedrive in Odoo.""",
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': "https://www.thrivebureau.com",
    'depends': ['base_setup'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/upload_file_views.xml',
        'views/onedrive_dashboard_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/onedrive_integration_thrive/static/src/js/onedrive.js',
            '/onedrive_integration_thrive/static/src/scss/onedrive.scss',
            '/onedrive_integration_thrive/static/src/xml/onedrive_dashboard.xml'
        ],
    },
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
    'uninstall_hook': 'uninstall_hook',
}
