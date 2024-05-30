# ©  2008-2018 Deltatech
# See README.rst file on addons root folder for license details


from thrive import _, api, fields, models
from thrive.exceptions import UserError


class ServicePriceChange(models.TransientModel):
    _name = "service.price.change"
    _description = "Service price change"

    @api.model
    def _default_currency(self):
        return self.env.user.company_id.currency_id

    product_id = fields.Many2one("product.product", string="Product", required=True, domain=[("type", "=", "service")])

    price_unit = fields.Float(string="Unit Price", required=True, digits="Service Price")

    currency_id = fields.Many2one("res.currency", string="Currency", required=True, default=_default_currency)
    reference = fields.Char("Reference")

    @api.model
    def default_get(self, fields_list):
        defaults = super().default_get(fields_list)
        active_ids = self.env.context.get("active_ids", False)
        if active_ids:
            cons = self.env["service.consumption"].browse(active_ids[0])
            defaults["product_id"] = cons.product_id.id
            defaults["price_unit"] = cons.price_unit
            defaults["currency_id"] = cons.currency_id.id
            defaults["reference"] = cons.name
        return defaults

    @api.onchange("product_id")
    def onchange_scanned_ean(self):
        price_unit = self.product_id.list_price
        from_currency = self.env.user.company_id.currency_id
        company = self.env.user.company_id
        to_currency = self.currency_id
        date = self._context.get("date") or fields.Date.today()
        self.price_unit = from_currency._convert(price_unit, to_currency, company, date)

    def do_price_change(self):
        active_ids = self.env.context.get("active_ids", False)

        if active_ids:
            domain = [("invoice_id", "=", False), ("product_id", "=", self.product_id.id), ("id", "in", active_ids)]
        else:
            domain = [("invoice_id", "=", False), ("product_id", "=", self.product_id.id)]

        consumptions = self.env["service.consumption"].search(domain)

        if not consumptions:
            raise UserError(_("No consumptions!"))  # , _("There were no service consumption !")

        consumptions.write({"price_unit": self.price_unit, "currency_id": self.currency_id.id, "name": self.reference})

        company = self.env.user.company_id
        to_currency = self.env.user.company_id.currency_id
        date = self._context.get("date") or fields.Date.today()

        price_unit = self.currency_id._convert(self.price_unit, to_currency, company, date)

        self.product_id.write({"list_price": price_unit})

        return {
            "domain": "[('id','in', [" + ",".join(map(str, [rec.id for rec in consumptions])) + "])]",
            "name": _("Service Consumption"),
            "view_type": "form",
            "view_mode": "tree,form",
            "res_model": "service.consumption",
            "view_id": False,
            "type": "ir.actions.act_window",
        }
