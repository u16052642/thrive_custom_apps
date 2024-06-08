# -*- coding: utf-8 -*-
###############################################################################
#
#  Thrive Bureaulogies Pvt. Ltd.
#
#  Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#  Author: Ranjith R (info@thrivebureau.com)
#
#  You can modify it under the terms of the GNU LESSER
#  GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#  You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#  (LGPL v3) along with this program.
#  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Website Tawk To',
    'version': '17.0.1.0.0',
    'category': 'Website',
    'summary': """Enhance real-time customer communication on your website with 
               Tawk.to Live Chat.""",
    'description': """This module integrates Tawk.to Live Chat into your Odoo 
               website, enabling real-time communication with visitors.""",
    'author': 'Thrive Bureau solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': 'https://www.thrivebureau.com',
    'depends': ['website'],
    'data': ['views/res_config_settings_views.xml'],
    'assets': {
        'web.assets_backend': [
            'website_tawk_to/static/src/js/website_tawk_to.js',
            'website_tawk_to/static/src/xml/website_tawk_to.xml']},
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
