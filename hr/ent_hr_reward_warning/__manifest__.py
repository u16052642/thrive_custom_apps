# -*- coding: utf-8 -*-
################################################################################
#
#    A part of OpenHRMS Project <https://www.openhrms.com>
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Thrive Bureau Solutions (info@thrivebureau.com)
#
#    This program is under the terms of the Odoo Proprietary License v1.0
#    (OPL-1)
#    It is forbidden to publish, distribute, sublicense, or sell copies of the
#    Software or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#    OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
#    USE OR OTHER DEALINGS IN THE SOFTWARE.
#
################################################################################
{
    'name': 'Enterprise Open HRMS Official Announcements',
    'version': '17.0.1.0.0',
    'category': 'Generic Modules/Human Resources',
    'summary': """Managing Official Announcements""",
    'description': """This module helps you to manage hr official announcements
     and Add Attachments to the announcement""",
    'live_test_url': 'https://www.youtube.com/watch?v=4gy3Jqn46SQ&feature=youtu.be',
    'author': "Thrive Bureau Solutions,Open HRMS",
    'company': 'Thrive Bureau Solutions',
    'website': "https://www.openhrms.com",
    'maintainer': 'Thrive Bureau Solutions',
    'depends': ['base', 'hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_announcement_security.xml',
        'data/ir_sequence_data.xml',
        'data/ir_cron_data.xml',
        'views/hr_announcement_views.xml',
        'views/hr_employee_views.xml'
    ],
    'demo': ['demo/hr_announcement_demo.xml'],
    'images': ['static/description/banner.jpg'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': False,
}
