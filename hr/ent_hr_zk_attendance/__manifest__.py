# -*- coding: utf-8 -*-
###############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Vyshnav AR (info@thrivebureau.com)
#
#   This program is under the terms of the Odoo Proprietary License v1.0 (OPL-1)
#    It is forbidden to publish, distribute, sublicense, or sell copies of the
#    Software or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL
#    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,ARISING
#    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
###############################################################################
{
    'name': 'Enterprise HRMS Biometric Device Integration',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'live_test_url': 'https://youtu.be/RHSHHU7nzTo',
    'summary': 'Integrating Biometric Device With HR Attendance (Face + Thumb)',
    'description': 'This module integrates Odoo with the biometric device'
                   '(Model: ZKteco uFace 202)',
    'author': 'Thrive Bureau Solutions, Mostafa Shokiel,Open HRMS',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': "https://www.thrivebureau.com",
    'depends': ['base_setup', 'hr_attendance'],
    'data': [
        'data/ir_cron_data.xml',
        'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
        'views/zk_machine_views.xml',
        'views/hr_attendance_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': False,
}
