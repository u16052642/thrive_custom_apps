# -*- coding: utf-8 -*-
################################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Jumana Haseen (info@thrivebureau.com)
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
################################################################################
{
    'name': 'One2Many Duplicate Records Widget',
    'version': '17.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'This widget is used to duplicating one2many records',
    'description': "This is a widget for one2many fields. By using this "
                   "widget we can duplicate records in one2many fields",
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': 'https://www.thrivebureau.com',
    'depends': ['base', 'web', 'sale'],
    'assets': {
        'web.assets_backend': [
            '/one2many_duplicate_record_widget/static/src/js/one2many_duplicate.js',
            '/one2many_duplicate_record_widget/static/src/xml/one2many_duplicate_templates.xml',
            '/one2many_duplicate_record_widget/static/src/css/InputBox.css',
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
