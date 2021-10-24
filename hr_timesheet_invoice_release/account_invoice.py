# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api, _
from odoo.exceptions import Warning


class AccountInvoice(models.Model):
    _inherit = 'account.move'


    def release_timesheet_lines(self):
        self.ensure_one()
        self.env['account.analytic.line'].search([
            ('move_id', '=', self.id)
        ]).with_context(override_check=True).write({'move_id': None})
