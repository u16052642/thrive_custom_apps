import logging
from thrive import fields, models, api, _

_logger = logging.getLogger(__name__)

class SNZettleSettings(models.Model):
    _name = 'sn.zettle.settings'
    _description = 'Simply NEAT Zettle User Settings'

    promotion_displayed = fields.Boolean('Promotion Displayed')

