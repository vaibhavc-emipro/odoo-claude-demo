# -*- coding: utf-8 -*-
{
    'name': "Demo Ept",
    'summary': "Simple demo module to track tasks",
    'description': """A minimal demo module with a single model, views and a menu.""",
    'author': 'Emipro Technologies Pvt. Ltd.',
    'website': 'http://www.emiprotechnologies.com',
    'maintainer': 'Emipro Technologies Pvt. Ltd.',
    'category': 'Tools',
    'version': '17.0.1.0.0',
    'license': 'OPL-1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/demo_task_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
