# -*- coding: utf-8 -*-
{
    'name': "1-debug My pet - viethai.io.vn",
    'summary': """My pet model""",
    'description': """Managing pet information""",
    'author': "viethai.io.vn",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        # 'views/my_pet_views.xml',
        'views/views.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
