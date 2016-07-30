# -*- coding: utf-8 -*-
{
    'name': '百度地图开发演示',
    'category': 'smartgo',
    'sequence': 10,
    'summary': 'SmartGo Baidu Map',
    'website': 'https://www.odoo.com/page/website-builder',
    'version': '1.0',
    'description': '',
    'depends': ['web', 'web_editor', 'web_planner'],
    'installable': True,
    'data': [
        'baidu_map_demo_view.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'application': True,
}
