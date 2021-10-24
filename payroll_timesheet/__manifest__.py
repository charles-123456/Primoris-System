# -*- coding: utf-8 -*-
{
    'name': "TimeSheet Based Payroll",
    'version': "14.0.1.0.0",
    'summary': """
        Payrolls Are Computed According to the Submitted & Confirmed Timesheets By Employees.""",
    'description': """
        Payrolls are computed according to the submitted and confirmed Timesheets By employees.
    """,

    'author': "Primoris Systems",
    'company': "Cybrosys Techno Solutions",
    'website':'https://www.primorissystems.com/',
    'category': "Generic Modules/Human Resources",
    'depends': ['hr_payroll','hr_contract','hr_timesheet','account','project','hr_timesheet_attendance'],
    'data': [
        'data/data.xml',
        'views/views.xml',
    ],
    'demo': [],
    'images': ['static/description/banner.jpg'],
    'license': "LGPL-3",
    'installable': True,
    'application': True
}
