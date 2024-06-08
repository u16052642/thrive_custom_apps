# -*- coding: utf-8 -*-
###############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Gayathri V (info@thrivebureau.com)
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
###############################################################################
from thrive import api, fields, models, _
from thrive.exceptions import UserError


class LegalTrial(models.Model):
    """This is used to the creation of legal trial"""
    _name = 'legal.trial'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Legal Trial'

    name = fields.Char(string="Name", readonly=True, default=lambda self: _('New'),
                       help='Trial number')
    case_id = fields.Many2one('case.registration', string="Case",
                              help='Corresponding case',
                              required=True,
                              domain="[('state', 'not in',"
                                     "['won', 'lost', 'invoiced'])]")
    client_id = fields.Many2one(related="case_id.client_id", string="Client",
                                readonly=False, required=True,
                                help='Client of the legal trial')
    trial_date = fields.Datetime(string="Trial Date", help='Date for trial',
                                 required=True)
    judge_id = fields.Many2one(related="case_id.judge_id", string="Judge",
                               readonly=False, help="Judge for "
                                                    "corresponding case")
    court_id = fields.Many2one(related="case_id.court_id", string="Court",
                               readonly=False, help="Court for "
                                                    "corresponding case")
    description = fields.Html(string="Description",
                              help="Description for the trail")
    is_invoiced = fields.Boolean(string='Is invoiced', help="Is trial invoiced",
                                 default=False)

    @api.model
    def create(self, vals):
        """Generate Sequence For Evidence"""
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'legal_trial') or 'New'
        return super().create(vals)

    @api.ondelete(at_uninstall=False)
    def _unlink_except_draft_or_cancel(self):
        """ Records can't be deleted"""
        raise UserError(_("You can not delete a trial"))
