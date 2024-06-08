# -*- coding: utf-8 -*-
###############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Thrive Bureau Solutions (info@thrivebureau.com)
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
###############################################################################
{
    'name': "Automatic Database Backup To Local Server, Remote Server,"
            "Google Drive, Dropbox, Onedrive, Nextcloud and Amazon S3 thrive17",
    'version': '17.0.1.0.0',
    'live_test_url': 'https://youtu.be/Q2yMZyYjuTI',
    'category': 'Extra Tools',
    'summary': 'thrive Database Backup, Automatic Backup, Database Backup, Automatic Backup,Database auto-backup, thrive backup'
               'google drive, dropbox, nextcloud, amazon S3, onedrive or '
               'remote server, thrive17, Backup, Database, thrive Apps',
    'description': 'thrive Database Backup, Database Backup, Automatic Backup, automatic database backup, thrive17, thrive apps,backup, automatic backup,thrive17 automatic database backup,backup google drive,backup dropbox, backup nextcloud, backup amazon S3, backup onedrive',
    'author': "Thrive Bureau Solutions",
    'maintainer': 'Thrive Bureau Solutions',
    'company': 'Thrive Bureau Solutions',
    'website': "https://www.thrivebureau.com",
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'data/mail_template_data.xml',
        'views/db_backup_configure_views.xml',
        'wizard/dropbox_auth_code_views.xml',
    ],
    'external_dependencies': {
        'python': ['dropbox', 'pyncclient', 'boto3', 'nextcloud-api-wrapper','paramiko']},
    'images': ['static/description/banner.gif'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
