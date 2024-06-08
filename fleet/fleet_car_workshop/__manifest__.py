# -*- coding: utf-8 -*-
###############################################################################
#
# Thrive Bureaulogies Pvt. Ltd.
#
# Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
# Author: Ayana KP (info@thrivebureau.com)
#
# You can modify it under the terms of the GNU AFFERO
# GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
# You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
# (AGPL v3) along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Car Workshop',
    'version': '17.0.1.0.0',
    'category': 'Industries',
    'summary': 'A Complete Vehicle Workshop Operations & Reports',
    'description': """This module helps to manage automobile workshop with
     great ease. Keep track of everything, like vehicle owner details,
     Works assigned, Bill details of service provided, etc.""",
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer ': 'Thrive Bureau Solutions',
    'website': "https://www.thrivebureau.com",
    'depends': ['fleet', 'stock', 'account'],
    'data': [
        'security/fleet_vehicle_security.xml',
        'security/ir.model.access.csv',
        'data/mail_message_subtype_data.xml',
        'data/ir_cron_data.xml',
        'views/car_workshop_views.xml',
        'views/vehicle_details_views.xml',
        'views/res_config_settings_views.xml',
        'views/material_used_views.xml',
        'views/worksheet_stages_views.xml',
        'views/worksheet_tag_views.xml',
        'views/car_workshop_reports.xml',

    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
