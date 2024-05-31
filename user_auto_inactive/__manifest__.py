# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'User Auto Inactive',
    'version': '17.0',
    'category': 'Extra Tools',
    'summary': 'User Auto Inactive based on last login is more than inactive days',
    'description': """
User Auto Inactive
===================
User Auto Inactive
""",
    'author': "Hariprasath.B",
    'website': 'www.linkedin.com/in/hari4274',
    'license': 'OPL-1',
    'currency': 'EUR',
    'depends': [
        'base',
        'base_setup',
    ],
    'data': [
        'data/data.xml',
        'views/res_config_settings_views.xml',
    ],
    'images': [
        'images/s1.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
