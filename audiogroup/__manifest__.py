# License AGPL-3 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Instance creator for AudioGroup',
    'summary': '''
    Instance creator for rroma. This is the app.
    ''',
    'author': 'Prointec',
    'license': 'AGPL-3',
    'category': 'Installer',
    'version': '14.0.1.0.0',
    'depends': [
        'sale',
    ],
    'data': [
        # views
        #'views/account_move.xml',
        # reports
        'reports/sale_order_templates.xml',
        #'reports/purchase_order_templates.xml',
        #'reports/sale_report_templates.xml',
        'reports/report_invoice.xml',
        #'reports/report_payment_receipt_templates.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
