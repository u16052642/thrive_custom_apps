# Copyright 2018 Mthrivelar <info@mthrivelar.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from thrive import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    password_expiration = fields.Integer(config_parameter="auth_password_policy.password_expiration", default=90)
    password_history = fields.Integer(config_parameter="auth_password_policy.password_history", default=0)
    password_lower = fields.Integer(config_parameter="auth_password_policy.password_lower", default=0)
    password_upper = fields.Integer(config_parameter="auth_password_policy.password_upper", default=0)
    password_numeric = fields.Integer(config_parameter="auth_password_policy.password_numeric", default=0)
    password_special = fields.Integer(config_parameter="auth_password_policy.password_special", default=0)
    test_password_expiration = fields.Boolean(
        "Test password expiration", config_parameter="auth_password_policy.test_password_expiration", default=False,
        help="If check it, time unit of password_expiration will be converted from days to minutes"
    )
