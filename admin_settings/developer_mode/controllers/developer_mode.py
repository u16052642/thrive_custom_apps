# -*- coding: utf-8 -*-
#############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Ayana KP (Contact : info@thrivebureau.com)
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
from thrive.http import request
from thrive.addons.web.controllers.home import Home


class AutoDeveloperMode(Home):
    """Custom Home class for automatic redirection to developer mode."""

    def _login_redirect(self, uid, redirect=None):
        """ If `redirect` is not provided, users belonging to the
        'developer_mode.developer_mode_group_user'
        group will be redirected to the developer mode, otherwise, they
        will be redirected to the default thrive dashboard."""
        if redirect:
            return redirect
        else:
            thrive_technician = request.env.user.has_group(
                'developer_mode.developer_mode_group_user')
            if thrive_technician:
                return '/web?debug=1'
            else:
                return '/web'
