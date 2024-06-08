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
    'name': 'Schedule Mail to Send',
    'version': '17.0.1.0.0',
    'category': 'Discuss',
    'summary': """Easily schedule your emails for future delivery""",
    'description': """This module provides a function or feature that allows 
    users to specify a future date and time for sending an email.""",
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': "https://www.thrivebureau.com",
    'depends': ['mail'],
    'data': [
        'data/ir_cron_data.xml',
        'data/mail_activity_type_data.xml',
        'views/mail_compose_message_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'schedule_mail_to_send/static/src/xml/mail_chatter.xml',
            'schedule_mail_to_send/static/src/js/chatter_topbar.js',
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
