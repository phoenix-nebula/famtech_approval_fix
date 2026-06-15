from odoo import models

class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    def message_post(self, *args, **kwargs):
        # Clean attachment_ids from kwargs
        if kwargs.get('attachment_ids'):
            kwargs['attachment_ids'] = [
                a for a in kwargs['attachment_ids']
                if a is not None and a is not False
            ]
            if not kwargs['attachment_ids']:
                kwargs.pop('attachment_ids')

        return super().message_post(*args, **kwargs)
