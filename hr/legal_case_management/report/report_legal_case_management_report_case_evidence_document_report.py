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
from thrive import models


class ReportLegalCaseManagementReportCaseEvidenceDocument(models.AbstractModel):
    """This is used to get the Evidence report"""
    _name = 'report.legal_case_management.report_case_evidence_document'
    _description = "Report For Evidence"

    def _get_report_values(self, docids, data=None):
        """Return the  Report Values For Evidence"""
        evidence_record = self.env['legal.evidence'].browse(docids)
        return {
            'evidence': evidence_record
        }
