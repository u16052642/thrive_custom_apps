# -*- coding: utf-8 -*-
################################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Vishnu KP(info@thrivebureau.com)
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
    'name': 'Draggable And Resizable Wizard',
    'version': '17.0.1.0.0',
    'summary': 'Draggable Wizard help to expand the wizard',
    'description': 'Make Every Backend Wizard In thrive Resizable And Draggable.',
    'category': 'Extra Tools',
    'author': 'Thrive Bureau solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'website': 'https://www.thrivebureau.com',
    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': [
            'dragable_and_resizable_wizard/static/src/css/dragable.css',
        ]
    },
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3'
}
