# -*- coding: utf-8 -*-
{
    "name": "AI Product Description Generator",
    "version": "17.0.1.0",
    "author": "Silver Touch Technologies Limited",
    'category': 'stock',
    "summary": "This module provides functionality of generating product description using AI",
    "website": "https://www.silvertouch.com/",
    "description": """
        """,
    'depends': ['product', 'sale_management'],
    'data': [
        'views/product_view.xml',
        'views/cron.xml',
        'views/custom_settings_field.xml',
    ],
    "price": 0,
    "currency": "USD",
    "license": "LGPL-3",
    'installable': True,
    'application': False,
    'images': ['static/description/banner.png']
}
