# -*- coding: utf-8 -*-
#############################################################################
#
#    Thrive Bureaulogies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Thrive Bureaulogies(<https://www.thrivebureau.com>)
#    Author:Anjhana A K(<https://www.thrivebureau.com>)
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
import json
from thrive import http
from thrive.http import content_disposition, request, serialize_exception as _serialize_exception
from thrive.tools import html_escape


class XLSXReportController(http.Controller):
    """ XLSX Report controller """

    @http.route('/xlsx_reports', type='http', auth='user',
                methods=['POST'], csrf=False)
    def get_report_xlsx(self, model, options, output_format,
                        report_name, **kw):
        """ Generate and retrieve an XLSX report. """
        options = json.loads(options)
        report_obj = request.env[model].with_user(request.session.uid)
        token = 'dummy-because-api-expects-one'
        try:
            if output_format == 'xlsx':
                response = request.make_response(
                    None,
                    headers=[('Content-Type', 'application/vnd.ms-excel'),
                             ('Content-Disposition', content_disposition(
                                 report_name + '.xlsx'))]
                )
                report_obj.get_xlsx_report(options, response)
            response.set_cookie('fileToken', token)
            return response
        except Exception as e:
            error = {
                'code': 200,
                'message': 'thrive Server Error',
                'data': _serialize_exception(e)
            }
            return request.make_response(html_escape(json.dumps(error)))
