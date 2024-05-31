# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import base64
import io
import logging
import os
import re

from thrive import api, fields, models, tools, _
from thrive.exceptions import ValidationError, UserError
from thrive.modules.module import get_resource_path

from random import randrange
from PIL import Image

_logger = logging.getLogger(__name__)


class Company(models.Model):
    _inherit = "res.company"
    
    is_school = fields.Boolean(string='School')