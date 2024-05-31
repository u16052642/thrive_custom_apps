# -*- coding: utf-8 -*-
from thrive import models, fields, api, _


class LoginImage(models.Model):
    _name = 'login.image'
    _rec_name = 'name'

    image = fields.Binary(string="Image")
    name = fields.Char(string="Name")
