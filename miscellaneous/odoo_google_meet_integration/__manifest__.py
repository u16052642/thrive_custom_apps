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
    'name': "Google Meet Calendar Integration",
    'version': '17.0.1.1.0',
    "category": 'Productivity',
    'summary': """A seamless integration solution for Google Meet within your calendar, 
    simplifying scheduling and access to virtual meetings.""",
    'description': """Enhance your scheduling efficiency with the Google Meet 
    Calendar Integration.This feature-rich application streamlines the process of 
    integrating Google Meet links into your calendar events, ensuring a smooth
     and hassle-free virtual meeting experience.""",
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': 'https://www.thrivebureau.com',
    'depends': ['contacts', 'calendar'],
    'data': [
        'views/res_company_views.xml',
        'views/calendar_event_views.xml'
    ],
    'images': ['static/description/banner.jpg'],
    'license': "LGPL-3",
    'installable': True,
    'auto_install': False,
    'application': False
}
