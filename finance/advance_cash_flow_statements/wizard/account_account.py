# -*- coding: utf-8 -*-
################################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
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
################################################################################
from thrive import api, models, fields
from thrive.tools.misc import get_lang


class Account(models.Model):
    _inherit = "account.report"
    _description = "Account Common Report"
    """This is used to inherit account report to add more fields and 
    functions"""

    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 readonly=True,
                                 default=lambda self: self.env.company,
                                 help='default Company')
    journal_ids = fields.Many2many(
        comodel_name='account.journal',
        string='Journals',
        required=True,
        default=lambda self: self.env['account.journal'].search(
            [('company_id', '=', self.company_id.id)]),
        domain="[('company_id', '=', company_id)]", help='Gives the journal of '
                                                         'the default company')
    date_from = fields.Date(string='Start Date',
                            help='Date at which report need to be start')
    date_to = fields.Date(string='End Date',
                          help='Date at which report need to be End')
    target_move = fields.Selection([('posted', 'All Posted Entries'),
                                    ('all', 'All Entries'),
                                    ], string='Target Moves', required=True,
                                   default='posted', help='Type of entries')

    @api.onchange('company_id')
    def _onchange_company_id(self):
        """ Fetch the journal values based on company"""
        if self.company_id:
            self.journal_ids = self.env['account.journal'].search(
                [('company_id', '=', self.company_id.id)])
        else:
            self.journal_ids = self.env['account.journal'].search([])

    def _build_contexts(self, data):
        """ Pass the context values for report"""
        result = {}
        result['journal_ids'] = 'journal_ids' in data['form'] and data['form'][
            'journal_ids'] or False
        result['state'] = 'target_move' in data['form'] and data['form'][
            'target_move'] or ''
        result['date_from'] = data['form']['date_from'] or False
        result['date_to'] = data['form']['date_to'] or False
        result['strict_range'] = True if result['date_from'] else False
        result['company_id'] = data['form']['company_id'][0] or False
        return result

    def _print_report(self, data):
        """ Report print action"""
        raise NotImplementedError()

    def check_report(self):
        """ Return the values for report"""
        self.ensure_one()
        data = {'ids': self.env.context.get('active_ids', []),
                'model': self.env.context.get('active_model', 'ir.ui.menu'),
                'form': self.read(
                    ['date_from', 'date_to', 'journal_ids', 'target_move',
                     'company_id'])[0]}
        used_context = self._build_contexts(data)
        data['form']['used_context'] = dict(used_context,
                                            lang=get_lang(self.env).code)
        return self.with_context(discard_logo_check=True)._print_report(data)
