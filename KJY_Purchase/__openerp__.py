# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': u'采购',
    'version': '0.1',
    'website': 'https://www.movdy.com',
    'category': u'采购',
    "author": u"KJY Development Team（feast）",
    'sequence': 1,
    'summary': u'包括采购单、采购明细',
    'description': u'包括采购单、采购明细',
    'depends': ['product', 'base', 'hr'],
    'data': [
        "view/kjy_purchase_menu.xml",
        "view/kjy_purchase_order_view.xml",
        "view/kjy_purchase_order_detailed_view.xml",
        "view/kjy_purchase_order_payment_view.xml",
    ],
    'test': [
    ],
    'demo': [
        'demo/toproerp_base_demo.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
}
