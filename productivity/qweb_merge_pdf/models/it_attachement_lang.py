from thrive import fields, models


class IrAttachmentLanguage(models.Model):
    _name = "ir.attachment.language"
    _description = "Attachment Language"

    mail_template_id = fields.Many2one(
        comodel_name="ir.actions.report",
        string="Template",
        required=True,
        ondelete="cascade",
    )

    lang = fields.Selection(
        selection=lambda self: self.env["res.lang"].get_installed(),
        string="Language",
        required=True,
    )

    attachment_ids = fields.Many2many(
        "ir.attachment",
        "attachment_report_rel",
        "report_id",
        "attachment_id",
        help="This Attachment is Merge with Qweb report and only support PDF attachments",
    )
