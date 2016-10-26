# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': u'采购',
    'version': '1.0',
    'summary': u'跨境翼的采购模块',
    'sequence': 1,
    'description': u"""
模块说明
====================
包括采购单、采购明细
   """,
    'category': 'KJY',
    'website': 'http://www.kjy.com',
    'images': [],
    'depends': ['product', 'base', 'hr'],
    'data': [
        "view/kjy_purchase_menu.xml",
        "view/sequences.xml",
        "view/kjy_purchase_order_view.xml",
        "view/kjy_purchase_order_detailed_view.xml",
        "view/kjy_purchase_order_payment_view.xml",
        "view/kjy_purchase_order_payment_type_view.xml",
        "view/kjy_purchase_order_cost_type_view.xml",
    ],
    'demo': [
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'post_init_hook': '_auto_install_l10n',
}
