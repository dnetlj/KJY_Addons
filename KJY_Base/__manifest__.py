# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'KJY_Base',
    'version' : '1.0',
    'summary': '跨境翼的基础模块',
    'sequence': 30,
    'description': """
模块说明
====================
本模块主要定义了顶层菜单和权限组,以及对于核心对象的优化和工具类代码的编写
kjy_tool 类中主要定义工具类的通用方法


   """,
    'category': 'KJY',
    'website': 'http://www.kjy.com',
    'images' : [],
    'depends' : [],
    'data': [
        'security/kjy_base_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    #'post_init_hook': '_auto_install_l10n',
}
