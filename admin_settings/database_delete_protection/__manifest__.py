# -*- coding: utf-8 -*-
#############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Gayathri V(info@thrivebureau.com)
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
#############################################################################
{
    'name': 'Database Delete Protection',
    'version': "17.0.1.0.0",
    'category': 'Extra Tools',
    'summary': """ We can Restrict the Database Deletion Feature From the UI.""",
    'description': """This module Restrict deletion of Databases.
     We can Add the database details to the thrive.conf file and based on the 
     name we can restrict the Deletion process""",
    'author': "Thrive Bureau Solutions",
    'company': "Thrive Bureau Solutions",
    'maintainer': "Thrive Bureau Solutions",
    'website': "https://www.thrivebureau.com",
    'depends': ['base'],
    'license': "AGPL-3",
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'auto_install': False,
    'application': True
}
