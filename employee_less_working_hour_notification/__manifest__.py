# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Anjhana A K (thrive@cybrosys.com)
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
    'name': "Employee Less Working Hour Notification",
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': ' Send Less Hours Worked Employees Details to HR',
    'description': 'Employee Less Working Hour Notification Mail App helps to '
                   'generate Email to HR which contains the list of employees'
                   ' who worked less than the time set in Configuration '
                   'Settings.',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['hr', 'hr_attendance'],
    'data': [
             'data/ir_cron_data.xml',
             'data/mail_template_data.xml',
             'views/res_config_settings_views.xml',
             ],
    'assets': {
        'web.assets_backend': [
            '/employee_less_working_hour_notification/static/src/css/style.css',
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
