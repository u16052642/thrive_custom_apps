# -*- coding: utf-8 -*-
#############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
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
############################################################################
{
    'name': "Catch Weight - Manufacturing",
    'version': '17.0.1.0.0',
    'category': 'Manufacturing',
    'summary': """Catch Weight Management In Manufacturing Module""",
    'description': """This Module lets us to enable Catch Weight Management
     System in Manufacturing Module""",
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': 'https://www.thrivebureau.com',
    'depends': ['base', 'mrp', 'mrp_subcontracting', 'stock', 'cw_stock', 'uom'],
    'data': [
        'views/mrp_bom_views.xml',
        'views/mrp_production_views.xml',
        'views/mrp_unbuild_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
