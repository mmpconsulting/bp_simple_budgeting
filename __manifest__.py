# -*- coding: utf-8 -*-
{
    'name': "Simple Budgeting",

    'summary': """
        Simple Budgeting""",

    'description': """
        Simple Budgeting, author : butirpadi, Phone: +6282398371826
    """,

    'author': "butirpadi",
    'website': "https://www.github.com/butirpadi",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'reports/report.xml',
        'reports/base_report.xml',
        'reports/budget_report.xml',
        'views/simple_budget_view.xml',
        'wizards/simple_budget_analysis_wizard_view.xml',
        'wizards/budget_analysis_line_view.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'installable': True,
}
