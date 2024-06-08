# -*- coding: utf-8 -*-
###############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Ranjith R (info@thrivebureau.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Project Task Timer',
    'version': '17.0.1.0.0',
    'category': 'Project',
    'summary': """Task Timer With Start & Stop""",
    'description': """This module helps you to track time sheet in project 
    automatically.""",
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': "http://www.thrivebureau.com",
    'depends': ['project', 'hr_timesheet'],
    'data': [
        'views/project_task_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'project_task_timer/static/src/css/style.css',
            'project_task_timer/static/src/js/timer.js',
            'project_task_timer/static/src/xml/timer.xml',
        ]},
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
