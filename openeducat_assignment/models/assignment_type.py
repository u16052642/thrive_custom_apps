# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    OpenEduCat Inc
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<https://www.openeducat.org>).
#
##############################################################################

from thrive import models, fields


class GradingAssigmentType(models.Model):
    _name = 'grading.assignment.type'
    _description = "Assignment Type"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
    assign_type = fields.Selection([('sub', 'Subjective'),
                                    ('attendance', 'Attendance')],
                                   string='Type', default='sub')
