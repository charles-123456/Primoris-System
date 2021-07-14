{
    'name': 'Custom Inventory Menu',
    'version': '14.0.1.0.0',
    'summary': 'Hour overview in invoice',
    'author': 'Primoris System',
    'website':'https://www.primorissystems.com/',
    'category': 'Stock Management',
    'depends': ['product','stock'],
    'data': [
            'views/project_template.xml',
            'views/inventory_inherit.xml',
            'views/manufacture_buy_menu.xml',
            'views/inprocess_menu.xml',
        ],
    'installable': True,
}