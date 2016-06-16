# -*- coding: utf-8 -*-
{
    'name': 'core',
    'category': 'smartgo',
    'sequence': 50,
    'summary': 'Build Your Enterprise Website',
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
        # 'views/website_templates.xml',
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
    'application': Flase,
}
