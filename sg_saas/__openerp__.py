# -*- coding: utf-8 -*-
{
    'name': 'SaaS Base Setup',
    'category': 'smartgo',
    'sequence': 20,
    'summary': 'saas base setup',
    'website': 'https://www.odoo.com/page/website-builder',
    'version': '1.0',
    'description': """
SmartGo Addons Core Modules
===========================

        """,
    'depends': ['web', 'web_editor', 'web_planner'],
    'installable': True,
    'data': [
        # 'data/data.xml',
        # 'data/web_planner_data.xml',
        # 'security/ir.model.access.csv',
        # 'security/ir_ui_view.xml',
        'views/res_users_view.xml',
        # 'views/website_views.xml',
        # 'views/snippets.xml',
        # 'views/res_config.xml',
        # 'views/ir_actions.xml',
        # 'views/website_backend_navbar.xml',
    ],
    'demo': [
        # 'data/demo.xml',
    ],
    'qweb': [
        # 'static/src/xml/website.backend.xml'
    ],
    'application': False,
}
