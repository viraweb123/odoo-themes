{
    "name": "VW Odoo Backend Theme",
    "description": """Minimalist and elegant backend theme for Odoo 14.""",
    "summary": "Dark Mode Backend Theme V14 is an attractive theme for backend",
    "category": "Themes/Backend",
    "version": "14.0.1.0.0",
    'author': 'ViraWeb123',
    'company': 'ViraWeb123',
    'maintainer': 'ViraWeb123',
    'website': "https://ViraWeb123.ir",
    "depends": ['base', 'web', 'mail'],
    "data": [
        'assets/assets.xml',
        'views/layout.xml',
    ],
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.png',
    ],
    'license': 'LGPL-3',
    'pre_init_hook': 'test_pre_init_hook',
    'post_init_hook': 'test_post_init_hook',
    'installable': True,
    'application': False,
    'auto_install': False,
}
