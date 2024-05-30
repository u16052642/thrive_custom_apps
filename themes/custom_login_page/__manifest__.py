# -*- coding: utf-8 -*-
################################################################################
#
#    Kolpolok Ltd. (https://www.kolpolok.com)
#    Author: Kolpolok (<https://www.kolpolok.com>)
#
################################################################################

{
    'name': "Custom Login Page",
    'version': '17.0.0.0',
    'summary': """This module assists in configuring a background image for the login page and hide other thrive elements""",
    'description': """Module helps to set background image in Login page.""",
    'license': 'LGPL-3',
    'website': "https://www.kolpoloktechnologies.com",
    'author': 'Kolpolok',
    'maintainer': 'Kolpolok',
    'category': 'Tools',
    'depends': ['base', 'portal'],
    'data': [
        'views/res_company.xml',
        'views/web_login.xml',
    ],
    'images': ['static/description/banner.png'],
    "application": True,
    "installable": True,
    "auto_install": False,
}
