# -*- coding: utf-8 -*-
#############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author:Anjhana A K(<https://www.thrivebureau.com>)
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
    'name': "Country-Based Terms and Condition",
    'version': '17.0.1.0.0',
    'description': """Customise your terms and condition based on  the country 
    of the contacts""",
    'summary': """This module helps to give terms and condition of the company 
    based on the customer's country""",
    'category': 'Extra Tools',
    'author': "Thrive Bureau Solutions",
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'depends': ['sale_management', 'contacts'],
    'data': [
        'views/res_country_views.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
