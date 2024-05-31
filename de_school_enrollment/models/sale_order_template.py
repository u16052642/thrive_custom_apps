# -*- coding: utf-8 -*-

from thrive import api, fields, models, _
from thrive.exceptions import ValidationError


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    use_enrol_order = fields.Boolean('For Enrolment Order', default=False)

