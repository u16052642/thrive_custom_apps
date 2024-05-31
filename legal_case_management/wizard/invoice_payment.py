# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Gayathri V (thrive@cybrosys.com)
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
from thrive import api, fields, models
from thrive.fields import Date


class InvoicePayment(models.TransientModel):
    """Create invoice for the case"""
    _name = 'invoice.payment'
    _description = 'Invoice Payment'

    case_id = fields.Many2one('case.registration', string='Case',
                              readonly=True, help='Case to create invoice')
    client_id = fields.Many2one(related='case_id.client_id', string='Client',
                                help='Clients for a case')
    lawyer_id = fields.Many2one(related='case_id.lawyer_id', string='Lawyer',
                                help='Lawyer for a case')
    date = fields.Date(string='Invoice Date', default=Date.today(),
                       readonly=True,
                       help='Today date')
    trial_ids = fields.Many2many('legal.trial', string="Trial")
    cost = fields.Float(string='Amount', help='Cost for invoice')
    is_trial_hide = fields.Boolean(string="Trial Hide", default=False,
                                   help="Ned to hide the trial?")
    is_cost_hide = fields.Boolean(string="Cost Hide", default=False,
                                  help="Need to hide the Cost?")
    is_last_trial = fields.Boolean(string="Last Trail",
                                   help="To identify the last trail",
                                   default=False)

    def create_invoice(self, price_unit, label):
        """Summary:
                Creates invoice.
           returns:
                 Corresponding invoices"""
        account_move_id = self.env['account.move'].create([{
            'move_type': 'out_invoice',
            'invoice_date': self.date,
            'partner_id': self.client_id.id,
            'case_ref': self.case_id.name,
            'invoice_line_ids': [(0, 0, {
                'name': label,
                'quantity': 1,
                'price_unit': price_unit,
            })],
        }])
        return {
            'name': 'Journal Entry',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'context': {'create': False},
            'view_mode': 'form',
            'res_id': account_move_id.id,
        }

    def print_invoice(self):
        """Print invoice for trial, case and out of court settlement"""
        if self.case_id.payment_method == 'case':
            self.case_id.write({'state': 'invoiced'})
            return self.create_invoice(label=self.case_id.name,
                                       price_unit=self.cost)
        elif self.case_id.payment_method == 'trial':
            for trial in self.trial_ids:
                trial.is_invoiced = True
            if self.is_last_trial is True:
                self.case_id.state = 'invoiced'
            invoiced_trials = self.trial_ids.mapped('name')
            cleaned_trial_ids = ", ".join(invoiced_trials).replace("[",
                                                                   "").replace(
                "]", "").replace("'", "")
            return self.create_invoice(
                label=cleaned_trial_ids,
                price_unit=self.cost * len(
                    self.trial_ids))
        else:
            self.case_id.write({'state': 'invoiced'})
            return self.create_invoice(label='Out of Court Settlement',
                                       price_unit=self.cost)

    @api.onchange('case_id')
    def _onchange_case_id(self):
        """Get cost per trial and case also for show corresponding trials
           in case"""
        self.is_trial_hide = True
        self.is_cost_hide = True
        if self.case_id.payment_method == 'trial':
            self.is_trial_hide = False
            trials = self.env['legal.trial'].search(
                [('case_id', '=', self.case_id.id),
                 ('is_invoiced', '=', False)])
            self.trial_ids = [(6, 0, trials.ids)]
            self.cost = self.lawyer_id.wage_per_trial
        elif self.case_id.payment_method == 'case':
            self.is_cost_hide = True
        else:
            self.is_cost_hide = False
