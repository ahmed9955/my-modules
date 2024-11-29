# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Contact Partner Type',
    'version': '18.0',
    'summary': 'Separate Customer and Vendors Contacts',
    'category': 'Contact',
    'description': """
        Separate Customers To be displayed 
        Only in sales and Vendors To be in Purchase
    """,
    'data': [
        'views/sale.xml',
        'views/contact.xml',
        'views/purchase.xml'
    ],
    'depends': [
        'contacts',
        'sale',
        'purchase',
        'account'
    ],
    'license': 'LGPL-3',
}
