# -*- coding: utf-8 -*-
################################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Sruthi Pavithran (info@thrivebureau.com)
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
################################################################################
{
    'name': "Add Product using Webcam Barcode in Pos",
    'version': '17.0.1.0.0',
    'category': 'Point of Sale',
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': 'https://www.thrivebureau.com',
    'summary': """Add the order-line using webcam scanner by adding barcode
     of products""",
    'description': """This module helps you to scan a product barcode using
     Webcam and add the products to pos order-line.""",
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_add_product_webcam_barcode/static/src/js/quagga.js',
            'pos_add_product_webcam_barcode/static/src/xml/barcode_dialog_templates.xml',
            'pos_add_product_webcam_barcode/static/src/js/pos_barcode.js',
            'pos_add_product_webcam_barcode/static/src/js/barcode_dialog.js',
            'pos_add_product_webcam_barcode/static/src/xml/pos_barcode_templates.xml',
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
