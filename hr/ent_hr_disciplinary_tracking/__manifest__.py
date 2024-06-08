# -*- coding: utf-8 -*-
######################################################################################
#
#    A part of Open HRMS Project <https://www.openhrms.com>
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Thrive Bureau Solutions (info@thrivebureau.com)
#
#    This program is under the terms of the Odoo Proprietary License v1.0 (OPL-1)
#    It is forbidden to publish, distribute, sublicense, or sell copies of the Software
#    or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
########################################################################################
{
    'name': 'Enterprise Open HRMS Disciplinary Tracking',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': """Employee Disciplinary Tracking Management 
    Reason/Action/Explanation""",
    'description': 'Allows to manage employee disciplinary records, can choose '
                   'disciplinary reason,action,employee explanation and shows '
                   'count of disciplinary records',
    'author': 'Thrive Bureau Solutions, Open HRMS',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': "https://www.openhrms.com",
    'depends': ['mail', 'hr',],
    'data': [
             'data/demo_data.xml',
             'security/ir.model.access.csv',
             'security/security.xml',
             'views/disciplinary_action_views.xml',
             'views/discipline_category_views.xml',
             ],
    'images': ['static/description/banner.jpg'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': False,
}
