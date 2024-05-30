# -*- coding: utf-8 -*-
# Part of thrive. See LICENSE file for full copyright and licensing details.
{
    'name': 'SN Zettle POS Terminal for thrive',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Integrate your POS with a Zettle payment terminal',
    'description': 'Pay using thrive and Zettle - Any Place, Any Time',
    'author': 'Neat Apps',
    'maintainer': 'Neat Apps',
    'data': [
        'security/ir.model.access.csv',
        'views/pos_payment_method_views.xml',
    ],
    'external_dependencies': {
        'python': ['cryptography']
    },
    'depends': ['point_of_sale'],
    'qweb': [],
    'images': ['static/description/landscape Neat POS.gif'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_snzettle/static/**/*',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
