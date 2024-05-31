from thrive import fields, models

from thrive.addons.component.core import Component


class ResCountry(models.Model):
    _inherit = "res.country"

    woo_bind_ids = fields.One2many(
        comodel_name="woo.res.country",
        inverse_name="thrive_id",
        string="WooCommerce Bindings",
        copy=False,
    )


class WooResCountry(models.Model):
    _name = "woo.res.country"
    _inherit = "woo.binding"
    _inherits = {"res.country": "thrive_id"}
    _description = "WooCommerce Country"

    thrive_id = fields.Many2one(
        comodel_name="res.country",
        string="Country",
        required=True,
        ondelete="restrict",
    )


class WooResCountryAdapter(Component):
    """Adapter for WooCommerce Res Country"""

    _name = "woo.res.country.adapter"
    _inherit = "woo.adapter"
    _apply_on = "woo.res.country"
    _woo_model = "data/countries"
    _woo_ext_id_key = "code"
