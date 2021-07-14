# -*- coding: utf-8 -*-
# © 2017 Sunflower IT (http://sunflowerweb.nl)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from itertools import groupby
import time
from datetime import datetime as dt

from odoo import fields, models, api, _
import odoo.addons.decimal_precision as dp
import itertools
import pprint
pp = pprint.PrettyPrinter(indent=4)

class AccountInvoice(models.Model):
    _inherit = 'account.move'

    report_analytic_lines = fields.One2many(comodel_name="account.analytic.line",
        inverse_name="timesheet_invoice_id", string="Analytic lines",
        help="The analytic lines coupled to this invoice.")
    hour_summary_invoice = fields.Boolean(string="Summary of Hours?", default=False)
    personal_info = fields.Boolean(string="Include Personal Info?", default=False)
    timesheet_sheet_id = fields.Many2one('hr_timesheet.sheet',string="Choose Timesheet Employee")
    value1 = fields.Text(string="Value1")

    def lines_per_project(self) :
        """ Return analytic lines per project """

        def grouplines(self, field='project_id'):
            for key, group in itertools.groupby(
                    self.sorted(lambda record : record[field].id),
                    lambda record : record[field]
            ):
                yield key, sum(group, self.browse([]))

        analytic_lines = self.report_analytic_lines

        for issue, lines in grouplines(analytic_lines, 'project_id') :
            print('issue',issue)
            print('lines',lines)
            yield {'category' : issue, 'lines':lines}


    def get_gst(self,inv_id,product_id):
        print('get_gst',inv_id)
        invoice = self.search([('id','=',inv_id)],limit=1)
        tax_amount = 0
        rate = 0

        for num in invoice.invoice_line_ids:
            if num.product_id.id == product_id:

                tax_rate = 0
                for i in num.tax_ids:

                    if i.children_tax_ids:
                        tax_rate = sum(i.children_tax_ids.mapped('amount'))

                tax_amount = ((tax_rate/100)*num.price_subtotal)/2
                rate = tax_rate/2
        return [rate,tax_amount]

    def get_igst(self, inv_id, product_id) :
        invoice = self.search([('id', '=', inv_id)], limit=1)
        tax_amount = 0
        rate = 0
        for i in invoice.invoice_line_ids :
            if i.product_id.id == product_id :
                tax_rate = 0
                for t in i.tax_ids :
                    if not t.children_tax_ids :
                        tax_rate = t.amount
                tax_amount = (tax_rate / 100) * i.price_subtotal
                rate = tax_rate
        return [rate, tax_amount]

    @api.onchange('timesheet_sheet_id')
    def _all_timesheet_obj(self) :
        value1 = []
        value_y = []
        sheet_obj = self.env['hr_timesheet.sheet'].search(
            [('employee_id', '=', self.timesheet_sheet_id.employee_id.id)])
        for obj in sheet_obj.line_ids :
            if obj.value_x not in value1 :
                value1.append(obj.value_x)
            value_y.append(obj.unit_amount)
            # value_y = set(value_y)
            print('valuex',value1)
            print('valuey',value_y)
            print('length',len(obj.value_x))
            print('length',len(obj.value_y))
        self.value1 = value1