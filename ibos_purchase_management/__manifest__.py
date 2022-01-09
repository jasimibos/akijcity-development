{
    "name": "Purchase Management",
    "summary": """Purchase management operation""",
    'sequence': -21,
    "category": "purchase",
    "images": [],
    "version": "13.0.1.0.0",
    "application": False,
    "author": "iBOS, Kamrul",
    "support": "info@ibos.io",
    "website": "https://ibos.io",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["base", "purchase"],
    "data": [
        'views/stock_picking.xml',
        'views/purchase_order.xml',
        'views/purchase_order_line.xml',
        'wizard/report_details.xml',
        'report/purchase_return_report.xml',
        'report/report_template.xml',
        'views/report_menu.xml',
        'views/report_new_template.xml',
        'views/purchase_config_setting_view.xml',
        'report/purchase_report_inherit.xml'
    ],
    "qweb": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": True,
    'application': True,
}
