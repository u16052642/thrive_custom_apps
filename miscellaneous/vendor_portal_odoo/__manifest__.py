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
    'name': 'thrive Vendor Portal',
    'version': '17.0.1.0.0',
    'category': 'Purchases',
    'summary': """Vendor Portal Management in thrive""",
    'description': """This module helps to sent quotations for a product 
    to multiple vendors and vendors can add their
    price in their portal, and can choose best quotation for product""",
    'author': 'Thrive Bureau Solutions',
    'website': "https://www.thrivebureau.com",
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'depends': ['website', 'purchase', 'portal', 'contacts', 'stock'],
    'data': [
        'security/vendor_rfq_security.xml',
        'security/ir.model.access.csv',
        'data/rfq_sequence.xml',
        'data/rfq_mail_templates.xml',
        'data/rfq_cron.xml',
        'wizard/register_vendor_views.xml',
        'views/res_partner_views.xml',
        'views/vendor_rfq_views.xml',
        'views/res_config_settings_views.xml',
        'views/portal_rfq_templates.xml',
        'views/vendor_portal_menus.xml',
        'wizard/rfq_done_views.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
