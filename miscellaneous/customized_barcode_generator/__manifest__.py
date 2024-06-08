# -*- coding: utf-8 -*-
###############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author:  Jumana Haseen (<https://www.thrivebureau.com>)
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
    'name': 'Customized Barcode Generator',
    'version': '17.0.1.0.0',
    'summary': """Print user defined product labels.""",
    'description': """The module enables user to print customized product
     labels, Barcode, Barcode Generator, Barcode Label, Product Label, 
     Product Barcode Generator, Product Barcode, Label Print, Product
      Label Print""",
    'category': 'Extra Tools',
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'depends': ['web', 'product', 'account'],
    'website': 'https://www.thrivebureau.com',
    'data': [
        'report/product_report_templates.xml',
        'security/ir.model.access.csv',
        'views/barcode_code_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
