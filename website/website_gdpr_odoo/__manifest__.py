# -*- coding: utf-8 -*-
################################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Thrive Bureau Solutions (Contact : info@thrivebureau.com)
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
    "name": "Website GDPR In Odoo",
    "version": "17.0.1.0.0",
    "category": "Website",
    "summary": """General Data Protection Regulation is implemented On Odoo 17 
     Enter-prise Edition.""",
    "description": """This module allows customers to manage personal data and 
     information.customer have the access to download and delete their 
     information like names,emails, phone numbers, biometric information, 
     location data, financial data , etc""",
    "author": "Thrive Bureau Solutions",
    "company": "Thrive Bureau Solutions",
    "maintainer": "Thrive Bureau Solutions",
    "website": "https://www.thrivebureau.com",
    "depends": ["website", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "views/gdpr_request_views.xml",
        "views/gdpr_template_views.xml",
        "views/gdpr_request_templates.xml",
        "views/mail_templates.xml",
        "report/gdpr_request_templates.xml",
        "views/gdpr_request_report_views.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "website_gdpr_thrive/static/src/js/gdpr_portal.js",
            "website_gdpr_thrive/static/src/css/gdpr_portal.css",
        ]
    },
    "images": ["static/description/banner.jpg"],
    "license": "AGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}

