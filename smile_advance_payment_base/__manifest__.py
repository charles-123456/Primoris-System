# -*- coding: utf-8 -*-
# (C) 2018 Smile (<http://www.smile.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Advance Payments - Base",
    "version": "14.0.1",
    "license": 'AGPL-3',
    "depends": ["account"],
    "author": "Primoris Systems",
    "description": """Supplier Advance Payments Management

Suggestions & Feedback to: Corentin Pouhet-Brunerie
    """,
    "website": "'https://www.primorissystems.com/'",
    "category": "Accounting & Finance",
    "sequence": 32,
    "data": [
        "security/ir.model.access.csv",
        "views/account_journal_view.xml",
        "views/account_payment_view.xml",
        "views/res_partner_view.xml",
    ],
    "demo": [],
    'test': [],
    "auto_install": False,
    "installable": True,
    "application": False,
}
