from odoo import models

class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    def write(self, vals):
        if 'attachment_ids' in vals:
            cleaned = []
            for cmd in vals['attachment_ids']:
                if isinstance(cmd, (list, tuple)) and len(cmd) == 3 and cmd[2] is None:
                    continue
                cleaned.append(cmd)
            vals['attachment_ids'] = cleaned
        return super().write(vals)
