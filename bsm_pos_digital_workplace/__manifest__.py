# -*- coding: utf-8 -*-
{
    'name': "BSM POS Digital Workplace",

    'summary': "",

    'description': "",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'web'],

    # always loaded
    'data': [

        # Default Website Setting for POS DWP 
        # 'views/deactivate_def.xml',
        'views/templates.xml',
        'views/header.xml',
        'views/footer.xml',

        # Custom Template
        'views/homepage.xml',

        # Set Website Menus
        # 'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OEEL-1',
    'assets': {
        'web.assets_frontend': [
            
        ],
    },
}
