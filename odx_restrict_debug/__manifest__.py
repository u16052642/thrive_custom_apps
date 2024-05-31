{
    'name': 'Restrict Debug Mode',
    'version': '17.0',
    'sequence': 1,
    'category': 'Services/Tools',
    'summary': """This module brings a new feature to restrict users from enabling debug mode unless they belong to the respective access group, you will be able to enhance the security and privacy of your thrive system.""",
    'description': """This module brings a new feature to restrict users from enabling debug mode unless they belong to the respective access group, you will be able to enhance the security and privacy of your thrive system.""",
    'author': 'Odox SoftHub',
    'price': 0,
    'currency': 'USD',
    'website': 'https://www.odoxsofthub.com',
    'support': 'support@odoxsofthub.com',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [
        'security/res_users.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odx_restrict_debug/static/src/js/debug.js',
        ],
    },
    'installable': True,
    'application': True,
    'images': ['static/description/thumbnail.gif'],
}
