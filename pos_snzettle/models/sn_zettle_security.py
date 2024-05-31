import logging
from thrive import fields, models, api, _
from cryptography.fernet import Fernet

_logger = logging.getLogger(__name__)

class PosPaymentMethod(models.Model):
    _name = 'sn.zettle.security'
    _description = 'Simply NEAT Zettle Security'

    sn_zettle_secret_key = fields.Char('Secret Key')

    def create(self, values):
        fernet_key = Fernet.generate_key()
        fernet_key_string = fernet_key.decode()
        values['sn_zettle_secret_key'] = fernet_key_string
        return super(PosPaymentMethod, self).create(values)


    def write(self, values):
        if 'sn_zettle_secret_key' in values:
            del values['sn_zettle_secret_key']
        return super(PosPaymentMethod, self).write(values)

