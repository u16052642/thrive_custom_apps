# -*- coding: utf-8 -*-
###############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Subina (info@thrivebureau.com)
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
    'name': 'Event Catering Service',
    'version': '17.0.1.0.0',
    "category": "Industries",
    'summary': """ Catering Service for Event Management Module.""",
    'description': """Event Catering attaches catering service to 
    Event Management module thus extending the scope of the Event Management 
    Module. When you install this module, a new service 'Catering' will be 
    available in event management. """,
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': "https://www.thrivebureau.com",
    'depends': ['event_management'],
    'data': ['security/event_catering_manager_groups.xml',
             'security/event_catering_security.xml',
             'security/ir.model.access.csv',
             'data/product_product_data.xml',
             'data/ir_sequence_data.xml',
             'views/event_management_catering_views.xml',
             'views/event_management_views.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
