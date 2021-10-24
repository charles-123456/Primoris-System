# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Hremployee(models.Model):
    _inherit = 'hr.employee'

    acc_number = fields.Char(string="A/C No.")
    ifsc_code = fields.Char(string="IFSC Code")
    bank_name = fields.Many2one('res.bank',string="Bank Name")
    branch_name = fields.Char(string="Branch")
    esi_number =  fields.Char(string="ESI NO")
    pf_number = fields.Char(string="PF NO")
    date_of_joining = fields.Date(string="DOJ")
    uan_number = fields.Char(string="UAN NO")
