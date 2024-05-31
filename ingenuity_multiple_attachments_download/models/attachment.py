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
from thrive import api, exceptions, fields, models, _


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    def action_download_attachment(self):
        # Download the attachment as Zip
        data_id = []
        for attachment in self:
            data_id.append(attachment.id)
        url = '/web/binary/download_document?tab_id=%s' % data_id
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new',
        }
