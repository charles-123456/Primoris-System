from odoo import models,fields,api,_
from odoo.exceptions import UserError

class TimesheetToInvoice(models.TransientModel):
    _name ="timesheet.to.invoice"

    @api.model
    def _count(self):
        return len(self._context.get('active_ids',[]))



    def create_invoice(self):
        inv_obj = self.env['account.analytic.line'].browse(self._context.get('active_ids',[]))
        for obj in inv_obj:
            var = [
                'Description:'+str(obj.name),
                'Project:'+str(obj.project_id.name),
                'Task:'+str(obj.task_id.name),
                'Amount:'+str(obj.unit_amount),
                'Date:'+str(obj.date),
                'Employee:'+str(obj.project_id.timesheet_ids.employee_id.name)]
            if self.is_description :
                var[0] = 'Description:' + str(obj.name)
            else :
                var[0] = ""
            if self.is_project :
                var[1] = 'Project:' + str(obj.project_id.name)
            else :
                var[1] = ""
            if self.is_task:
                var[2] = 'Task:' + str(obj.task_id.name)
            else :
                var[2] = ""
            if self.is_hour :
                var[3] = 'Hour:' + str(obj.unit_amount)
            else :
                var[3] = ""
            if self.is_date:
                var[4] = 'Date:' + str(obj.date)
            else:
                var[4]=""
            if self.is_task:
                var[5] = "Employee:" + str(obj.project_id.timesheet_ids.employee_id.name)
            else:
                var[5] = ""
            while ("" in var):
                var.remove("")
            name = "\n".join(map(lambda x : str(x) or "", var))
            invoice_vals = {
                'ref' : obj.ref,
                # 'name': 'Draft',
                'move_type' : 'out_invoice',
                'l10n_in_gst_treatment':'regular',
                'invoice_origin' : obj.name,
                'invoice_user_id' : obj.user_id.id,
                'partner_id' : obj.project_id.partner_id.id,
                'journal_id':self.journal_id.id,
                'currency_id' : self.currency_id.id,
                'state':'draft',
                'partner_bank_id':obj.company_id.partner_id.bank_ids[:1].id,
                'invoice_line_ids' : [(0, 0, {
                    'name': name,
                    'quantity' :obj.unit_amount,
                    'price_unit':obj.project_id.timesheet_cost,
                    'product_id' : self.invoice_product_id.id,
                    'product_uom_id' : obj.product_uom_id.id,
                })],

            }
            # print('values',invoice_vals)
            invoice_exist_check = obj.mapped('invoice_id.id')
            duplicate = obj.search([('invoice_id','=',invoice_exist_check)])
            # print('duplicate',duplicate)
            if duplicate:
                raise UserError(_('You Cannot create Invoice already timesheet invoiced record!!!'))
            else:
                 invoice =self.env['account.move'].sudo().create(invoice_vals).with_user(self.env.uid)
            # print('invoice',invoice)
            invoice._compute_name()
            res=[]
            res.append((invoice.id,invoice.name))
            # print('res',res)
            # print('res[]',res[0])
            obj.write({'invoice_id':res[0]})
            invoice.message_post_with_view('mail.message_origin_link',
                                           values={'self' : invoice, 'origin' : obj},

                                           subtype_id=self.env.ref('mail.mt_note').id)

        return invoice



    @api.onchange('is_project')
    def _onchange_values(self):
        if self.is_project:
            self.is_project = True

    @api.onchange('is_task')
    def _onchange_task(self):
        if self.is_task:
            self.is_task = True

    @api.onchange('is_hour')
    def _onchange_hour(self):
        if self.is_hour:
            self.is_hour = True

    @api.onchange('is_description')
    def _onchange_description(self):
        if self.is_description:
            self.is_description = True


    count = fields.Integer(default=_count,readonly=True,string="Order Count")
    journal_id = fields.Many2one('account.journal',string="Journal")
    invoice_product_id = fields.Many2one('product.product',string="Invoice Product")
    currency_id = fields.Many2one('res.currency',string="currency")
    is_project = fields.Boolean(string="Project",default=False)
    is_task = fields.Boolean(string="Task",default=False)
    is_description = fields.Boolean(string="Description",default=False)
    is_hour = fields.Boolean(string="Hour",default=False)
    is_date = fields.Boolean(string="Date",default=False)
    is_employee = fields.Boolean(string="Employee",default=False)
    merge = fields.Boolean(string='Merge', default=False)

