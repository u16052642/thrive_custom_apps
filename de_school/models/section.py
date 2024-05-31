# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from thrive import api, fields, models, _
from thrive.exceptions import UserError, AccessError

class SchoolSection(models.Model):
    _name = 'oe.school.course.section'
    _description = 'Course Section'
    
    name = fields.Char(string='Course', required=True, index=True, translate=True) 
    course_id = fields.Many2one('oe.school.course', string='Course', required=True)
