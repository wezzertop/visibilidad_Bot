{
    'name': 'Visibilidad de Bots (Livechat)',
    'version': '18.0.1.0.0',
    'category': 'Website/Livechat',
    'summary': 'Controla la visibilidad de los canales de Livechat (bots) para usuarios autenticados y no autenticados.',
    'description': """
Visibilidad de Bots (Livechat)
==============================
En Odoo Community, los bots de chat aparecen por defecto en las páginas sin permitirte limitarlos a ciertos perfiles de usuario.
Este módulo soluciona ese problema permitiéndote configurar la visibilidad de tus canales de Livechat y Bots. 
Puedes restringir los bots para que solo aparezcan a usuarios registrados, a ciertos perfiles específicos o mantenerlos públicos.
¡Toma el control de tu Livechat!
    """,
    'author': 'JDDM',
    'depends': ['im_livechat'],
    'data': [
        'views/im_livechat_channel_views.xml',
        'views/bot_menus.xml',
    ],
    'images': ['static/description/icon.png'],
    'price': 15.00,
    'currency': 'USD',
    'installable': True,
    'application': True,
    'license': 'OPL-1',
}
