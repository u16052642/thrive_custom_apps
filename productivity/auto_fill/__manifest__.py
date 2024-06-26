# -*- coding: utf-8 -*-
###############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Farhana Jahan PT (info@thrivebureau.com)
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
###############################################################################
{
    'name': 'Auto Fill',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Widget that suggests field value from existing records""",
    'description': 'Widget for auto completing a character field according'
                   ' to its existing record values',
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
	'maintainer': 'Thrive Bureau Solutions',
    'website': "https://www.thrivebureau.com",
    'assets': {
        'web.assets_backend': {
            '/auto_fill/static/src/css/auto_fill.css',
            '/auto_fill/static/src/js/auto_fill.js',
            '/auto_fill/static/src/xml/auto_fill.xml',
        },
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
