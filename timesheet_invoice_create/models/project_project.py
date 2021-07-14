from odoo import models,fields,api

class InheritedNewProject(models.Model):
    _inherit = "project.project"

    employee_id = fields.Many2one('hr.employee',string="Employee")
    timesheet_cost = fields.Monetary(related='employee_id.timesheet_cost',string="Rate Per Hour")

