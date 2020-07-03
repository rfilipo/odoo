# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Kobkob Theme',
    'description': 'Kobkob themes',
    'category': 'Theme/Technology',
    'sequence': 1100,
    'version': '1.0',
    'author': 'Monsenhor',
    'depends': ['website', 'website_theme_install'],
    'data': [
        'views/theme_kobkob_templates.xml',
        'views/assets.xml',
    ],
    'images': [
        'static/description/kobkob.png',
        'static/description/kobkob_screenshot.jpg',
    ],
    'application': False,
}
