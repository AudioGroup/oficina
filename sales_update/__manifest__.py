# -*- coding: utf-8 -*-
{

    'name': "xSales update ",
    'version': '14e',
    'category': 'Extras',
    'summary': 'Ajustes y mejoras en Ventas',
    'description': """
        Mejoras al módulo de Contización  
        1. Agrega campo de direccion de entrega, en cotización y el reporte

    """,
    'author': 'Prointec S.A.',
    'website': 'http://www.prointeccr.com',
    'depends': ['sale'],
    'data': [
        'report/sale_report_templates.xml',
        'views/sale_views.xml'
    ],
    'application': False,
    'installable': True,
    'auto_install': False,    
}