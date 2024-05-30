# ©  2023 Deltatech
# See README.rst file on addons root folder for license details

from thrive import api, fields, models


class BusinessDevelopment(models.Model):
    _name = "business.development"
    _description = "Business Development"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
    description = fields.Text(string="Description")
    area_id = fields.Many2one(string="Business area", comodel_name="business.area", required=True)
    type_id = fields.Many2one(string="Type", comodel_name="business.development.type", required=True)

    project_id = fields.Many2one(string="Project", comodel_name="business.project")
    approved = fields.Selection(
        [("draft", "Draft"), ("approved", "Approved"), ("rejected", "Rejected"), ("pending", "Pending")],
        string="Approved",
        default="draft",
        tracking=True,
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("specification", "Specification"),
            ("development", "Development"),
            ("test", "Test"),
            ("production", "Production"),
        ],
        string="State",
        default="draft",
        tracking=True,
    )

    responsible_id = fields.Many2one(
        string="Consultant", domain="[('is_company', '=', False)]", comodel_name="res.partner"
    )
    date_start_fs = fields.Date(string="Start FS", help="Start date functional specification")
    date_end_fs = fields.Date(string="End FS", help="End date functional specification")
    completion_fs = fields.Float(
        string="Completion FS",
        help="Completion of functional specification",
        group_operator="avg",
    )
    effort_fs = fields.Float(string="Effort FS", help="Effort for functional specification")

    developer_id = fields.Many2one(
        string="Developer", domain="[('is_company', '=', False)]", comodel_name="res.partner"
    )
    date_start_dev = fields.Date(help="Start date development")
    date_end_dev = fields.Date(help="End date development")
    completion_dev = fields.Float(
        help="Completion development",
        group_operator="avg",
    )
    effort_dev = fields.Float(string="Effort Dev", help="Effort for development")

    tester_id = fields.Many2one(string="Tester", domain="[('is_company', '=', False)]", comodel_name="res.partner")
    date_start_test = fields.Date(help="Start date test")
    date_end_test = fields.Date(help="End date test")
    completion_test = fields.Float(
        help="Completion test",
        group_operator="avg",
    )
    effort_test = fields.Float(string="Effort Test", help="Effort for test")

    customer_id = fields.Many2one(string="Customer", comodel_name="res.partner")

    @api.model
    def create(self, vals):
        if not vals.get("code", False):
            vals["code"] = self.env["ir.sequence"].next_by_code(self._name)
        result = super().create(vals)
        return result

    def name_get(self):
        self.browse(self.ids).read(["name", "code"])
        return [
            (development.id, "{}{}".format(development.code and "[%s] " % development.code or "", development.name))
            for development in self
        ]
