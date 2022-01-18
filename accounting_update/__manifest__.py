# -*- coding: utf-8 -*-
{

    'name': "xAccouting update ",
    'version': '14e',
    'category': 'Extras',
    'summary': 'Ajustes y mejoras en Contabilidad',
    'description': """
        1. Agregar campo de direccion de entrega y partida arancelaria a reporte de factura.

    """,
    'author': 'Prointec S.A.',
    'website': 'http://www.prointeccr.com',
    'depends': ['sale'],
    'data': [
        'report/report_invoice_inherit.xml'
    ],
    'application': False,
    'installable': True,
    'auto_install': False,    
}