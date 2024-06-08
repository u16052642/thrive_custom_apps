# -*- coding: utf-8 -*-
################################################################################
#
#    A part of OpenHRMS Project <https://www.openhrms.com>
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>).
#    Author: Thrive Bureau Solutions (info@thrivebureau.com)
#
#    This program is under the terms of the Odoo Proprietary License v1.0
#    (OPL-1)
#    It is forbidden to publish, distribute, sublicense, or sell copies of the
#    Software or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#    OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
#    USE OR OTHER DEALINGS IN THE SOFTWARE.
#
################################################################################
from thrive import fields, models


class HrContract(models.Model):
    """ Model adding notice period days in hr_contract. """
    _inherit = 'hr.contract'

    def _get_default_notice_days(self):
        """ Method for return notice days. """
        if self.env['ir.config_parameter'].sudo().get_param(
                'hr_resignation.notice_period'):
            return self.env['ir.config_parameter'].sudo().get_param(
                            'hr_resignation.no_of_days')
        else:
            return 0

    notice_days = fields.Integer(string="Notice Period",
                                 help="Notice Days",
                                 default=_get_default_notice_days)
