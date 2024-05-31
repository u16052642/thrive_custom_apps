# -*- coding: utf-8 -*-
# Part of Browseinfo. See LICENSE file for full copyright and licensing details.

from thrive  import api, fields, models, _
from datetime import datetime, time
import pytz
from thrive.exceptions import UserError,ValidationError




class my_equipment_request(models.Model):
    _name = "overtime.request"
    _rec_name = "employee_id"
    _description = "Overtime Request"



    def _compute_num_of_hours(self):
        self.num_of_hours = 0.0
        for line in self :          
            if line.start_date and line.end_date :
                diff  = line.end_date - line.start_date
                days, seconds = diff.days, diff.seconds
                hours = days * 24 + seconds // 3600
                line.num_of_hours = hours
        return

    employee_id = fields.Many2one('hr.employee',string="Employee" ,required=True)
    start_date = fields.Datetime(string="Start Date",required=True,default=fields.datetime.now())
    end_date = fields.Datetime(string="End Date",required=True)
    department_id = fields.Many2one('hr.department',string="Department")
    department_manager_id = fields.Many2one('hr.employee',string="Manager")
    include_in_payroll = fields.Boolean(string = "Include In Payroll",default=True)
    
    approve_date = fields.Datetime(string="Approve Date",readonly=True)
    approve_by_id = fields.Many2one('res.users',string="Approve By",readonly=True)

    dept_approve_date = fields.Datetime(string="Department Approve Date",readonly=True)
    dept_manager_id = fields.Many2one('res.users',string="Department Manager",readonly=True)

    num_of_hours = fields.Float(string="Number Of Hours",compute="_compute_num_of_hours")

    notes = fields.Text(string="Notes")

    state = fields.Selection([('new','New'),('first_approve','Waiting For First Approve'),('dept_approve','Waiting For Department Approve'),
                                ('done','Done'),('refuse','Refuse')],string="State",default='new')


    @api.constrains('end_date','start_date')
    def check_end_date(self):
        if self.end_date < self.start_date :
            raise ValidationError(_('End Date must be after the Start Date!!'))



    @api.onchange('employee_id')
    def onchange_employee(self):

        self.department_id = self.employee_id.department_id.id
        self.department_manager_id = self.employee_id.department_id.manager_id.id
        
        
    def confirm_action(self):

        self.write({'state' : 'first_approve'})
        return

    def first_approve_action(self):
        self.write({'state' : 'dept_approve',
                    'approve_by_id' : self.env.user.id,
                    'approve_date' : fields.datetime.now()})        
        return

    def dept_approve_action(self):
        self.write({'state' : 'done',
                    'dept_manager_id' : self.env.user.id,
                    'dept_approve_date' : fields.datetime.now()})       
        return


    def refuse_action(self):
        self.write({'state' : 'refuse'})
        return


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def _get_worked_day_lines_values(self, domain=None):
        res = super()._get_worked_day_lines_values(domain=domain)

        start_date = datetime.strptime(str(self.date_from), "%Y-%m-%d")
        date_obj = datetime.strptime(str(self.date_to), "%Y-%m-%d")
        max_datetime = datetime.combine(date_obj, time.max)
        overtime = self.env['overtime.request'].search([('state', '=', 'done'), ('start_date', '>=', start_date),
                                                        ('end_date', '<=', max_datetime),
                                                        ('employee_id', '=', self.employee_id.id)])
        overtime_total = self.employee_id.get_overtime(self.employee_id.id,start_date,max_datetime)
        work_entry_type = self.env['hr.work.entry.type'].search([('code', '=', 'OVERTIME')], limit=1)
        seq = 0
        if overtime:
            seq += 1
            res.append({
                'sequence': seq,
                'work_entry_type_id': work_entry_type.id,
                'number_of_days': len(overtime.mapped('num_of_hours')),
                'number_of_hours': overtime_total,
                'code': 'OVERTIME',
                'name': 'Overtime',
                'payslip_id': self.id
            })
        return res


