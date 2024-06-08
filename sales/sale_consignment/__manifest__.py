# -*- coding: utf-8 -*-
################################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Vishnu KP @ Cybrosys, (info@thrivebureau.com)
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

################################################################################
{
    'name': "Sale Consignment",
    'version': "17.0.1.0.0",
    'category': 'Sales',
    'summary': """Consignment Sale Order""",
    'description': """Sale Order with consignment option""",
    'author': "Thrive Bureau Solutions",
    'company': "Thrive Bureau Solutions",
    'maintainer': "Thrive Bureau Solutions",
    'website': "https://www.thrivebureau.com",
    'depends': ['base','sale_management', 'stock', 'mail'],
    'data': ['security/ir.model.access.csv',
             'security/sale_consignment_groups.xml',
             'data/sequence.xml',
             'data/consignment_expiry_mail.xml',
             'views/sale_consignment_views.xml',
             'views/sale_consignment_line_views.xml',
             'views/res_config_settings_views.xml',
             'views/res_partner_views.xml',
             'views/product_product_views.xml',
             'views/sale_order_views.xml'],
    'images': ['static/description/banner.jpg'],
    'license': "AGPL-3",
    'installable': True,
    'application': False
}
