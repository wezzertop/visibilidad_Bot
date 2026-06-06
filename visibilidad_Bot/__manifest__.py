{
    'name': 'Bot Visibility (Livechat)',
    'version': '18.0.1.0.0',
    'category': 'Website/Livechat',
    'summary': 'Controls the visibility of Livechat channels (bots) for authenticated and unauthenticated users.',
    'description': """
Bot Visibility (Livechat)
==============================
In Odoo Community, chat bots appear by default on pages without allowing you to limit them to certain user profiles.
This module solves that problem by allowing you to configure the visibility of your Livechat channels and Bots.
You can restrict bots so that they only appear to registered users, specific profiles, or keep them public.
Take control of your Livechat!
    """,
    'author': 'JDDM',
    'depends': ['im_livechat'],
    'data': [
        'views/im_livechat_channel_views.xml',
        'views/bot_menus.xml',
    ],
    'images': ['static/description/banner.gif', 'static/description/icon.png'],
    'price': 5.00,
    'currency': 'USD',
    'installable': True,
    'application': True,
    'license': 'OPL-1',
}
