# -*- coding: utf-8 -*-
################################################################################
#
#    Ogroni Informatix Limited
#
#    Copyright (C) 2024-TODAY Ogroni Informatix Limited(<https://www.ogroni.com/>).
#    Author: Billal (billal.hossain@ogroni.com)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

{
    'name': "Custom Login Style",
    'category': 'Extra Tools',
    'version': '17.0.1.0.0',
    'author': 'Ogroni Informatix Limited',
    'maintainer': 'Ogroni Informatix Limited',
    'company': 'Ogroni Informatix Limited',
    'website': 'https://www.ogroni.com',
    'depends': ['base', 'base_setup', 'web'],
    'summary': """Empower users to personalize their thrive login experience with customizable background colors, images,
     and alignments, fostering a unique and engaging interface.""",
    'description': """
       Elevate your thrive platform's aesthetic appeal by allowing users to effortlessly 
       customize login page elements, including background colors, images, and alignments, 
       ensuring a personalized and visually captivating experience.
    """,
    'data': [
        'views/res_config_settings_views.xml',
        'views/webclient_templates_right.xml',
        'views/webclient_templates_left.xml',
        'views/webclient_templates_middle.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
