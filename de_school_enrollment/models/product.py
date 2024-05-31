# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import logging

from thrive import api, fields, models, _
from thrive.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP
from thrive.exceptions import ValidationError
from thrive.tools.float_utils import float_round

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    fee_product = fields.Boolean("Fee Product")