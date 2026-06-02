from odoo import models, fields, api

class ImLivechatChannel(models.Model):
    _inherit = 'im_livechat.channel'

    bot_visibility = fields.Selection([
        ('all', 'Todos (Públicos y Autenticados)'),
        ('public', 'Solo Públicos (No Autenticados)'),
        ('authenticated', 'Solo Autenticados'),
    ], string='Visibilidad del Bot', default='all', required=True,
       help='Define qué usuarios pueden ver e interactuar con este bot en el sitio web.')
