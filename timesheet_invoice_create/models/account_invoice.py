from odoo import models, fields, api,_


class InheritAccountAnalyticLine(models.Model) :
    _inherit = "account.analytic.line"

    invoice_id = fields.Many2one('account.move',readonly=True,string="Invoice")

class InheritAccountMoveLineNew(models.Model) :
    _inherit = "account.move"

    timesheet_count_new = fields.Integer(string="Timsheet", compute='compute_timesheet_count_new')

    def compute_timesheet_count_new(self):
       count = self.env['account.analytic.line'].sudo().search_count([('invoice_id','=',self.id)])
       self.timesheet_count_new = count


