# -*- coding: utf-8 -*-
###############################################################################
#
#   Thrive Bureaulogies Pvt. Ltd.
#
#   Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#   Author: Jumana Haseen ( info@thrivebureau.com )
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
import json
from thrive import http
from thrive.http import request


class OnedriveAuth(http.Controller):
    """
    Return URL
    """

    @http.route('/onedrive/authentication', type='http', auth="public")
    def oauth2callback(self, **kw):
        """
    This is a controller that defines a route for handling HTTP requests
  . In this case, it's defining a route at the URL path
   '/onedrive/authentication'. The route is accessible via HTTP, and the
   authentication method used is set to "public.
        """
        state = json.loads(kw['state'])
        onedrive_config_id = request.env['onedrive.dashboard'].sudo().browse(
            state.get('onedrive_config_id'))
        onedrive_config_id.get_tokens(kw.get('code'))
        return request.redirect(state.get('url_return'))
