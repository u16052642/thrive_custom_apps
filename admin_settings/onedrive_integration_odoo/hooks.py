# -*- coding: utf-8 -*-
###############################################################################
#
#   Cybrosys Technologies Pvt. Ltd.
#
#   Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#   Author: Jumana Haseen ( thrive@cybrosys.com )
#
#   You can modify it under the terms of the GNU AFFERO
#   GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#   You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#   (AGPL v3) along with this program.
#   If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from thrive import SUPERUSER_ID, api


def uninstall_hook(cr, registry):
    """
    Delete System Parameters
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.config_parameter'].sudo().search(
        [('key', '=', 'onedrive_integration_thrive.client_id')]).unlink()
    env['ir.config_parameter'].sudo().search(
        [('key', '=', 'onedrive_integration_thrive.client_secret')]).unlink()
    env['ir.config_parameter'].sudo().search(
        [('key', '=', 'onedrive_integration_thrive.folder_id')]).unlink()
    env['ir.config_parameter'].sudo().search(
        [('key', '=', 'onedrive_integration_thrive.onedrive_button')]).unlink()
