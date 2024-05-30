# coding: utf-8
# Part of thrive. See LICENSE file for full copyright and licensing details.
import json
import logging
import pprint
import random
import requests
import string
from werkzeug.exceptions import Forbidden
from datetime import datetime
from werkzeug.security import generate_password_hash
from thrive import fields, models, api, _
from thrive.exceptions import ValidationError
import secrets
import re

_logger = logging.getLogger(__name__)

class PosPaymentMethod(models.Model):
    _inherit = 'pos.payment.method'

    def _get_payment_terminal_selection(self):
        return super(PosPaymentMethod, self)._get_payment_terminal_selection() + [('snzettle', 'SN Zettle Terminal')]

    sn_zettle_terminal_device_code = fields.Char('Terminal ID', help='This is a uniquely generated identifier upon creation for each terminal used to login. The same Terminal ID should never be used for more than 1 terminal')
    sn_zettle_terminal_master_pwd = fields.Char('Terminal Master Password', help='', groups="base.group_erp_manager")
    sn_zettle_terminal_master_pwd_mock = fields.Char('Terminal Master Password', help='Password used to login in the terminal', default='', groups="base.group_erp_manager")
    sn_zettle_is_mobile = fields.Boolean(string='Use Mobile Redirect', help="Indicates if you will use thrive on the mobile device that has the SN Zettle POS app so it can improve the user experience by redirecting to the app when needed.")
    sn_zettle_terminal_pass_uuid = fields.Char('Terminal Pass UUID')

    sn_zettle_device_type = fields.Selection(
        [('android', 'Android'), ('ios', 'iOS')],
        string='Device Type',
        help='Indicates what operating system the terminal will use. Example: If the SN Zettle POS App is installed on an Android then Android should be selected here.'
    )
    @api.model
    def _get_user_groups(self):
        ir_model_data = self.env['ir.model.data']
        groups = ir_model_data.search([('model', '=', 'res.groups')])
        return [(group.complete_name, group.name) for group in groups]

    sn_zettle_terminal_manager_group_selection = fields.Selection(
        selection=_get_user_groups,
        string='Manager Group',
        help='Select a manager group that will be able to override payments that need resending.',
    )

    @api.model
    def create(self, values):
        if values['use_payment_terminal'] == 'snzettle':
            if values['sn_zettle_terminal_master_pwd_mock'] is False or values['sn_zettle_terminal_master_pwd_mock'] == '' or len(
                values['sn_zettle_terminal_master_pwd_mock']) < 6:
                raise ValidationError("Master Password must have at least 6 characters.")
            values['sn_zettle_terminal_pass_uuid'] = self.generate_password_uuid()
            hashed_password = generate_password_hash(values['sn_zettle_terminal_master_pwd_mock'])
            values['sn_zettle_terminal_master_pwd'] = hashed_password
            values['sn_zettle_terminal_device_code'] = self.generate_unique_datetime_id()
            del values['sn_zettle_terminal_master_pwd_mock']
        return super(PosPaymentMethod, self).create(values)

    def write(self, values):
        if 'sn_zettle_terminal_device_code' in values:
            del values['sn_zettle_terminal_device_code']
        if 'sn_zettle_terminal_master_pwd_mock' in values:
            if values['sn_zettle_terminal_master_pwd_mock'] is False or values[
                'sn_zettle_terminal_master_pwd_mock'] == '' or len(
                    values['sn_zettle_terminal_master_pwd_mock']) < 6:
                raise ValidationError("Master Password must have at least 6 characters.")
            values['sn_zettle_terminal_pass_uuid'] = self.generate_password_uuid()
            hashed_password = generate_password_hash(values['sn_zettle_terminal_master_pwd_mock'])
            values['sn_zettle_terminal_master_pwd'] = hashed_password
            del values['sn_zettle_terminal_master_pwd_mock']

        return super(PosPaymentMethod, self).write(values)

    def generate_password_uuid(self):
        return datetime.utcnow().strftime('%Y%m%d%H%M%S') + str(random.randint(1000, 9999))

    def generate_unique_datetime_id(self):
        while True:
            # Generate a datetime string with milliseconds and the full year
            current_datetime = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]

            # Replace numbers with corresponding letters for uneven indexes
            transformed_id = ''.join(
                [chr(ord('a') + int(char)) if index % 2 != 0 else char for index, char in enumerate(current_datetime)])

            # Insert dashes every 3 characters
            formatted_id = '-'.join([transformed_id[i:i+3] for i in range(0, len(transformed_id), 3)])

            # Check if the generated ID already exists in the database
            existing_record = self.search([('sn_zettle_terminal_device_code', '=', formatted_id)])

            # If no matching record found, return the unique ID
            if not existing_record:
                return formatted_id

