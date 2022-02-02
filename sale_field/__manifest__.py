# -*- coding: utf-8 -*-
{
    'name': "sale_field",

    'summary': """purchase order field in sale order""",

    'description': """
    """,

    'author': "SURSOOM",
    'website': "http://www.sursoom.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management','account_accountant'],

    # always loaded
    'data': [
#        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
 #       'demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
