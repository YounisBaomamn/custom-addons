# -*- coding: utf-8 -*-
{
    'name': "Care Card",

    'summary': """
       Create a care card for the beneficiary
       """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Younis Bamoman",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'security/groups_rules.xml',
        'data/data_cron.xml',
        'data/Sequence_nmber.xml',
        'views/template_static.xml',
        'views/care_card.xml',
        'views/update_card_request.xml',
        'views/card_request.xml',
        'views/create_care_template.xml',
        'views/card_info_template.xml',
        'views/update_card_request_template.xml',
        'views/sending_request_email_template.xml',
        'data/websiti.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
