# -*- coding: utf-8 -*-
################################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Bhagyadev KP (info@thrivebureau.com)
#
#    This program is under the terms of thrive Proprietary License v1.0 (OPL-1)
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
################################################################################
{
    'name': 'Lot and Serial Number Expiry Report',
    'version': '17.0.1.0.0',
    'category': 'Warehouse',
    'summary': """Generates a detailed Lot and Serial Number Expiry based on 
     their expiry details.""",
    'description': """This module helps you to print a report about tracking
     products (lot/serial) based on their expiry date. You can filter your
     report based on different criteria.""",
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': 'https://www.thrivebureau.com',
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        'report/product_batch_report_reports.xml',
        'report/product_batch_report_templates.xml',
        'wizard/product_batch_report_views.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': False,
}
