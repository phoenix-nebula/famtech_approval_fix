from odoo import models

class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    def message_post(self, **kwargs):
        # Fix: filter out None values from attachment_ids
        # caused by a bug in Odoo 18 core Approvals app
        if 'attachment_ids' in kwargs:
            kwargs['attachment_ids'] = [
                a for a in kwargs['attachment_ids'] if a is not None
            ]
        return super().message_post(**kwargs)
