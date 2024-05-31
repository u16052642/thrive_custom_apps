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

from thrive import api, fields, models


class ResConfigSettings(models.TransientModel):
    """Inherits 'res.config.settings' to add fields for customize login page."""
    _inherit = 'res.config.settings'

    orientation = fields.Selection(selection=[('default', 'Default'),
                                              ('left', 'Left'),
                                              ('middle', 'Middle'),
                                              ('right', 'Right')],
                                   string="Orientation",
                                   help="Type of login page visibility",
                                   config_parameter="og-app-custom-login-page.orientation")
    background = fields.Selection(selection=[('color', 'Color Picker'),
                                             ('image', 'Image'),
                                             ('url', 'URL')],
                                  string="Background",
                                  help="Background of the login page",
                                  config_parameter="og-app-custom-login-page.background")
    image = fields.Binary(string="Image", help="Select background image "
                                               "of login page")
    url = fields.Char(string="URL", help="Select and url of image",
                      config_parameter="og-app-custom-login-page.url")
    color = fields.Char(string="Color", help="Set a colour for background "
                                             "of login page",
                        config_parameter="og-app-custom-login-page.color")

    @api.model
    def get_values(self):
        """Super the get_values function to get the field values."""
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(image=params.get_param('og-app-custom-login-page.image'))
        return res

    def set_values(self):
        """Super the set_values function to save the field values."""
        super(ResConfigSettings, self).set_values()
        params = self.env['ir.config_parameter'].sudo()
        params.set_param('og-app-custom-login-page.image', self.image)

    @api.onchange('orientation')
    def onchange_orientation(self):
        """Set background field to false for hiding option to customize login
           page background """
        if self.orientation == 'default':
            self.background = False
