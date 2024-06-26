# -*- coding: utf-8 -*-
###############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author: Vishnu KP S (info@thrivebureau.com)
#
#    This program is under the terms of the thrive Proprietary License v1.0 (OPL-1)
#    It is forbidden to publish, distribute, sublicense, or sell copies of the
#    Software or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL
#    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,ARISING
#    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
###############################################################################
from thrive import fields, models


class MobileComplaint(models.Model):
    """This model represents for the mobile Complaint type managing"""
    _name = 'mobile.complaint'
    _description = 'Mobile Complaint'
    _rec_name = 'complaint_type'

    complaint_type = fields.Char(string="Complaint Type", required=True,
                                 help="This field specifies the type of the "
                                      "complaint.")