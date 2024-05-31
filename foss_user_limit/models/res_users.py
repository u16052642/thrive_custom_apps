# -*- coding: utf-8 -*-
# Part of thrive. See LICENSE file for full copyright and licensing details.

from thrive import fields, api, models, _
from thrive.exceptions import ValidationError


class Users(models.Model):
    _inherit = "res.users"

    @api.model
    def create(self, vals):
        Config = self.env["ir.config_parameter"].sudo()
        database_user_limit = Config.get_param("database_user_limit", None)        
        res = super(Users, self).create(vals)
        no_of_users = self.search_count([])
        if int(no_of_users) > int(database_user_limit):
            raise ValidationError('Warning! \nAllowed user limit exceeded!!, Please contact system administrator!!')
        return res

    def write(self, vals):
        Config = self.env["ir.config_parameter"].sudo()
        database_user_limit = Config.get_param("database_user_limit", None)        
        res = super(Users, self).write(vals)
        no_of_users = self.search_count([])
        if int(no_of_users) > int(database_user_limit):
            raise ValidationError('Warning! \nAllowed user limit exceeded!!, Please contact system administrator!!')
        return res





