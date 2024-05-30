# -*- coding: utf-8 -*-
#############################################################################
#
#    Ingenuity Info
#
#    Copyright (C) 2023-TODAY Ingenuity Info(<https://ingenuityinfo.in>)
#    Author: Ingenuity Info(<https://ingenuityinfo.in>)
#
#
#############################################################################
import logging
import zipfile
import ast
from thrive import http
from thrive.http import request
from thrive.http import content_disposition
from datetime import datetime
try:
    from BytesIO import BytesIO
except ImportError:
    from io import BytesIO
_logger = logging.getLogger(__name__)


class Binary(http.Controller):

    # Controller to download the Zip
    @http.route('/web/binary/download_document', type='http', auth="public")
    def download_document(self, tab_id, **kw):
        sec_window = ast.literal_eval(tab_id)
        attachment_ids = request.env['ir.attachment'].sudo().search([('id', 'in', sec_window)])

        # File Preparations
        file_data_dict = {}
        for attachment_id in attachment_ids:
            file_data_store = attachment_id.store_fname
            if file_data_store:
                file_name = attachment_id.name
                file_path = attachment_id._full_path(file_data_store)
                file_data_dict["%s:%s" % (file_data_store, file_name)] = dict(path=file_path, name=file_name)

        # Zip Conversation
        zip_filename = datetime.now()
        zip_filename = "%s.zip" % zip_filename
        bitIO = BytesIO()
        zip_file = zipfile.ZipFile(bitIO, "w", zipfile.ZIP_DEFLATED)
        for file_info in file_data_dict.values():
            zip_file.write(file_info["path"], file_info["name"])
        zip_file.close()
        
        return request.make_response(bitIO.getvalue(), headers=[('Content-Type', 'application/x-zip-compressed'), ('Content-Disposition', content_disposition(zip_filename))])