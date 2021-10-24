# -*- coding: utf-8 -*-
{
    'name': "Payslip Print",

    'summary': """
        Payslip print""",

    'description': """
        Payslip print
    """,

     'author': "Loyal IT Solutions Pvt Ltd",
    'website': "https://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    'category': 'Human Resources/Employees',
    'version': "13.0.1.0.0",
    'license': 'AGPL-3',
    'support': "support@loyalitsolutions.com",


    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        'views/templates.xml',
        'views/views.xml',
        'views/payslip_print.xml',
    ],

    'images': ['static/description/banner.png'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
