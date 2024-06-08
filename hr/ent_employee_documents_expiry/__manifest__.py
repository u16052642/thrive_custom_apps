# -*- coding: utf-8 -*-
################################################################################
#
#    A part of OpenHRMS Project <https://www.openhrms.com>
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Thrive Bureau Solutions (info@thrivebureau.com)
#
#    This program is under the terms of the thrive Proprietary License v1.0
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
    'name': 'Enterprise Open HRMS Employee Documents',
    'version': '17.0.1.0.0',
    'category': 'Generic Modules/Human Resources',
    'summary': """Manages Employee Documents With Expiry Notifications.""",
    'description': """This module Manages Employee Related Documents with 
     Expiry Notifications.Employee documents with such necessary information 
     must be saved and used accordingly.This module helps to  store and manage
     the employee related documents like certificates, appraisal reports, 
     passport,license etc""",
    'live_test_url': 'https://www.youtube.com/watch?v=Wc__1NkMHko&feature=youtu.be',
    'author': "Thrive Bureau Solutions,Open HRMS",
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': "https://www.openhrms.com",
    'depends': ['hr'],
    'data': [
        'data/ir_cron_data.xml',
        'security/ir.model.access.csv',
        'views/hr_document_views.xml',
        'views/document_type_views.xml',
        'views/hr_employee_document_views.xml',
        'views/hr_employee_views.xml',
    ],
    'demo': [
        'data/document_type_demo.xml',
        'data/hr_work_location_demo.xml',
        'data/hr_employee_demo.xml',
        'data/hr_employee_document_demo.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': False,
}
