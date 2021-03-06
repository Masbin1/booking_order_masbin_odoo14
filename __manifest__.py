# -*- coding: utf-8 -*-
{
    'name': "Booking Order Odoo 14",

    'summary': """
        Booking Order odoo 14""",

    'description': """
        Booking Order odoo 14
    """,

    'author': "Masbin",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/wizard_cancelled.xml',
        'views/service_team_views.xml',
        'views/work_order_views.xml',
        'views/booking_order_views.xml',
        'views/menu.xml',
        'report/report_work_order.xml',
        'report/report.xml',
        'data/data.xml',
    ],
}
