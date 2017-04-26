# -*- coding: utf-8 -*-
{
    'name': "educasge",

    'summary': """
        Modulo que crea un listado de alumnos""",

    'description': """
        Modulo educasge, crea un listado de alumnos. Modulo creado para la asignatura
        Sistemas de gestión empresarial en el grado superior de desarrollo de aplicaciones
         multiplataforma.
    """,

    'author': "Iñaki Diaz",
    'website': "http://www.IñakiDiaz.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}