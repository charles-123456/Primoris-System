# -*- encoding: utf-8 -*-
{
    'name': 'Timesheet Invoice Create',
    'version': '14.0.1.0.0',
    'summary': 'Timesheet ',
    'author': 'Primoris Systems ',
    'website': 'https://www.primorissystems.com/',
    'category': 'Sales Management',
    'depends': ['sale_timesheet','hr_timesheet','account','project'],
    'data': [
            'security/ir.model.access.csv',
            'security/timesheet.xml',
            'views/project_inherit.xml',
            'views/account_analytic_line.xml',
            'views/account_move.xml',
             'wizard/timesheet_make_invoice_view.xml',
        ],
    'installable': True,
}
