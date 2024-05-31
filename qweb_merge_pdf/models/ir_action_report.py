import base64
import io
import logging

import lxml.html
from PIL import ImageFile
from PyPDF2 import PdfFileReader, PdfFileWriter

from thrive import fields, models

ImageFile.LOAD_TRUNCATED_IMAGES = True

_logger = logging.getLogger(__name__)


class IrActionsReport(models.Model):
    _inherit = "ir.actions.report"

    ir_attachment_language_ids = fields.One2many(
        string="Language Dependent Attachments",
        comodel_name="ir.attachment.language",
        inverse_name="mail_template_id",
    )

    def join_pdf(self, pdf_chunks):
        # Create empty pdf-writer object for adding all pages here
        result_pdf = PdfFileWriter()

        # Iterate for all pdf-bytes
        for chunk in pdf_chunks:
            # Read bytes
            chunk_pdf = PdfFileReader(
                stream=io.BytesIO(initial_bytes=chunk)  # Create steam object
            )
            # Add all pages to our result
            for page in range(chunk_pdf.getNumPages()):
                result_pdf.addPage(chunk_pdf.getPage(page))

        # Writes all bytes to bytes-stream
        response_bytes_stream = io.BytesIO()
        result_pdf.write(response_bytes_stream)
        return response_bytes_stream.getvalue()

    def _run_wkhtmltopdf(
        self,
        bodies,
        report_ref,
        header=None,
        footer=None,
        landscape=False,
        specific_paperformat_args=None,
        set_viewport_size=False,
    ):
        res = super()._run_wkhtmltopdf(
            bodies,
            report_ref,
            header,
            footer,
            landscape,
            specific_paperformat_args,
            set_viewport_size,
        )
        report_sudo = self._get_report(report_ref)
        language = specific_paperformat_args.get("partner_lang")
        for attachment in report_sudo.ir_attachment_language_ids:
            for att in attachment.attachment_ids:
                if att.mimetype == "application/pdf" and attachment.lang == language:
                    res = self.join_pdf([res, base64.b64decode(att.datas)])
        return res

    def _prepare_html(self, html, report_model):
        language = self.env.user.lang or "en_US"
        root = lxml.html.fromstring(html)
        match_class = (
            "//div[contains(concat(' ', normalize-space(@class), ' '), ' {} ')]"
        )
        for node in root.xpath(match_class.format("article")):
            if node.get("data-oe-lang"):
                language = node.get("data-oe-lang")
        (
            bodies,
            res_ids,
            header,
            footer,
            specific_paperformat_args,
        ) = super()._prepare_html(html, report_model)
        specific_paperformat_args.update({"partner_lang": language})
        return bodies, res_ids, header, footer, specific_paperformat_args
