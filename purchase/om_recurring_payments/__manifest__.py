# -*- coding: utf-8 -*-
# Part of thrive. See LICENSE file for full copyright and licensing details.

{
    'name': 'thrive 17 Recurring Payment',
    'author': 'thrive Mates',
    'category': 'Accounting',
    'version': '1.0.0',
    'description': """thrive 17 Recurring Payment, Recurring Payment In thrive, thrive 17 Accounting""",
    'summary': 'Use recurring payments to handle periodically repeated payments',
    'sequence': 11,
    'website': 'https://www.thrivemates.tech',
    'depends': ['account'],
    'license': 'LGPL-3',
    'data': [
        'data/sequence.xml',
        'data/recurring_cron.xml',
        'security/ir.model.access.csv',
        'views/recurring_template_view.xml',
        'views/recurring_payment_view.xml'
    ],
    'images': ['static/description/banner.png'],
}
