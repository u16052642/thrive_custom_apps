# -*- coding: utf-8 -*-
{
    'name': 'Tele Biometric Device Integration',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': "Integrating Biometric Device (Model: ZKteco uFace 202) With HR"
               "Attendance (Face + Thumb)",
    'description': "This module integrates Odoo with the biometric"
                   "device(Model: ZKteco uFace 202),thrive17,thrive,hr,attendance",
    'author': 'TeleNoc',
    'company': 'TeleNoc',
    'maintainer': 'TeleNoc',
    'website': "https://www.telenoc.org",
    'depends': ['base_setup', 'hr_attendance'],
    'data': [
        'security/ir.model.access.csv',
        'views/biometric_device_details_views.xml',
        'views/hr_employee_views.xml',
        'views/daily_attendance_views.xml',
        'views/biometric_device_attendance_menus.xml',
    ],
    'images': ['static/description/banner.jpeg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
