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
    "name": "All In One HTML Notes",
    "version": "17.0.1.0.0",
    "category": "Accounting,Purchases,Sales,Warehouse",
    "summary": """To use HTML notes in sales,purchase,invoice and inventory""",
    "description": "Addon for setup HTML notes in configuration and used this"
    "default notes or customized notes in sales,purchase, "
    "invoice and inventory form view and also use this notes "
    "in reports",
    "author": "Thrive Bureau Solutions",
    "company": "Thrive Bureau Solutions",
    "maintainer": "Thrive Bureau Solutions",
    "website": "https://www.thrivebureau.com",
    "depends": ["sale_management", "stock", "purchase"],
    "data": [
        "views/account_move_views.xml",
        "views/res_config_settings_views.xml",
        "views/sale_order_views.xml",
        "views/purchase_order_views.xml",
        "report/sale_order_templates.xml",
        "report/purchase_order_templates.xml",
        "report/account_move_templates.xml",
        "report/stock_picking_templates.xml",
    ],
    "images": ["static/description/banner.jpg"],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}
