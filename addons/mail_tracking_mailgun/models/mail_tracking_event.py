# Copyright 2017 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MailTrackingEvent(models.Model):
    _inherit = "mail.tracking.event"

    mailgun_id = fields.Char(string="Mailgun Event ID", copy="False", readonly=True)

    def _process_data(self, tracking_email, metadata, event_type, state):
        res = super()._process_data(tracking_email, metadata, event_type, state)
        res.update({"mailgun_id": metadata.get("mailgun_id", False)})
        return res
