{
    "name": "Partial/Credit Payment",
    "summary": """Partial/Credit Payment""",
    'sequence': -28,
    "category": "Point Of Sale",
    "images": [],
    "version": "13.0.1.0.3",
    "application": False,
    "author": "iBOS, Kamrul, Mridul",
    "support": "info@ibos.io",
    "website": "https://ibos.io",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["base", "point_of_sale", "ibos_employee_to_customer"],
    "data": [
        'view/Assets.xml',
        'view/pos_config_view.xml',
        'view/pos_order_from_view.xml',
        'view/res_partner.xml',
        'view/pos_order_tree_view.xml',
    ],
    "qweb": ["static/src/xml/pos_payment.xml"],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": True,
    'application': True,
}