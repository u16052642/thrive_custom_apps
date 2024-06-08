# -*- coding: utf-8 -*-
###############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Mohammed Dilshad Tk (info@thrivebureau.com)
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
    'name': 'Export Attachments From List View',
    'version': '17.0.1.0.0',
    'category': 'Document Management',
    'summary': 'The module used to download multiple record attachment easily',
    'description': 'When using dynamic functionality in this model,'
                   'the module can be used to quickly download the documents '
                   'in multiple records. Documents related to documents and'
                   ' other attachments are attached to the selected records '
                   'that downloaded quickly.',
    'author': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'maintainer': 'Thrive Bureau Solutions',
    'website': 'https://www.thrivebureau.com',
    'depends': ['base', 'base_setup'],
    'data': [
        'security/ir.model.access.csv',
        'views/export_attachment_views.xml',
        'views/res_config_settings_views.xml',
        'wizard/attachment_download_confirmation_views.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
