# -*- coding: utf-8 -*-
# from odoo import http


# class HrPayslipPrint(http.Controller):
#     @http.route('/hr_payslip_print/hr_payslip_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_payslip_print/hr_payslip_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_payslip_print.listing', {
#             'root': '/hr_payslip_print/hr_payslip_print',
#             'objects': http.request.env['hr_payslip_print.hr_payslip_print'].search([]),
#         })

#     @http.route('/hr_payslip_print/hr_payslip_print/objects/<model("hr_payslip_print.hr_payslip_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_payslip_print.object', {
#             'object': obj
#         })
