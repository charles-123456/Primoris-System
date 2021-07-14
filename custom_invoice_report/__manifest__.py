{
    'name': 'Custom Invoice Report',
    'version': '14.0.1.0.0',
    'summary': 'Hour overview in invoice',
    'author': 'Primoris System',
    'website':'https://www.primorissystems.com/',
    'category': 'Sales Management',
    'depends': ['hr_timesheet','account','sale_timesheet','product','stock'],
    'data': [
            'report/invoice.xml',
            'views/project_task_inherit.xml',
            'views/account_invoice_view.xml',
            'report/account_invoice_report.xml',
            'report/invoice_report.xml',
        ],
    'installable': True,
}