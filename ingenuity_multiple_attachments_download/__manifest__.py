# -*- coding: utf-8 -*-
#############################################################################
#
#    Ingenuity Info
#
#    Copyright (C) 2023-TODAY Ingenuity Info(<https://ingenuityinfo.in>)
#    Author: Ingenuity Info(<https://ingenuityinfo.in>)
#
#
#############################################################################
{
    'name': "Download Multiple Attachments",
    'author': "Ingenuity Info",
    'category': 'Tools',
    'summary': """ This module will allow you to Download Multiple Attachments on Single Clicks. Select your Attachments and click on the Action -> Download button.""",
    'website': "https://ingenuityinfo.in",
    'company': 'Ingenuity Info',
    'maintainer': 'Ingenuity Info',
    'version': '17.0.0.0',
    'price': 0.0,
    'currency': 'EUR',
    'description': """ Select Attachments and click on an Action button on top, It has a sub-button called Download. Separate menu with name Attachment, You can Search for the document and apply filters according to your need. Create a Zip file of the selected records and download it.
    """,
    'depends': [
        'base',
    ],
    'data': [
        'views/attachment_views.xml',
    ],
    'qweb': [
    ],
    'images': ['static/description/Banner.gif'],
    'license': "LGPL-3",
    'external_dependencies': {
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
