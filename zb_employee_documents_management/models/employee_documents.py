# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2024 ZestyBeanz Technologies(<http://www.zbeanztech.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from thrive import _, api, fields, models
from datetime import timedelta, date,datetime
from collections import defaultdict


class EmployeeDocuments(models.Model):
    _name = "employee.documents"
    _inherit = ['mail.thread']
    _description = "Employee Documents"
    _rec_name = "employee_id"
    
    name = fields.Char('Name')
    desciption = fields.Text('Description')
    expiry = fields.Date('Expiry',tracking=True)
    attachment = fields.Binary('Attachment')
    type_id = fields.Many2one('employee.document.type', string='Type')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    file_name = fields.Char('File Name')
    doc_number = fields.Char('Document No',required=True)
    
    _sql_constraints = [('unique_code_doc_number', 'unique(doc_number)', 'Document Number Should be Unique!')]
    
    
    
    def send_document_expiry_reminder(self):
        documents_data = self.get_documents_data()
        ctx = self.env.context.copy()
        settings = self.env['res.config.settings'].create({})
        to_mail = settings.doc_expiry_to_mail
        cc_mail = settings.doc_expiry_cc_mail
        email_values = {
            'email_to': to_mail,
            'email_cc': cc_mail,
        }
        if documents_data['types']:
            template = self.env.ref('zb_employee_documents_management.document_expiry_email_reminder')
            template.with_context(ctx).send_mail(self.id, email_values=email_values, force_send=True)
    
    def get_documents_data(self):
        today = fields.Date.today()
        one_month_later = today + timedelta(days=30)
        expiring_docs = self.env['employee.documents'].search([('expiry', '>=', today), ('expiry', '<=', one_month_later)])
        types = expiring_docs.mapped('type_id')
        docs_by_type_list = []
        for type in types:
            employee_list = []
            docs = expiring_docs.filtered(lambda s: s.type_id == type)
            for doc in docs:
                vals = {
                    'name': doc.employee_id.name,
                    'doc_number': doc.doc_number,
                    'expiry_date': doc.expiry
                    }
                employee_list.append(vals)
            docs_by_type = {
                'type':type.name,
                'employees':employee_list,
                }
            docs_by_type_list.append(docs_by_type)
        values = {'types':docs_by_type_list}
        return values
        
           
    
    
class EmployeeDocumentType(models.Model):
    _name = "employee.document.type"
    _description = "Employee Document Type"
    _rec_name = "name"
    
    
    name = fields.Char('Name')
    
    