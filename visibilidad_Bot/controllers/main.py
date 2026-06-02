from odoo import http
from odoo.http import request
from odoo.addons.im_livechat.controllers.main import LivechatController

class VisibilidadBotLivechatController(LivechatController):

    @http.route('/im_livechat/init', type='json', auth="public")
    def livechat_init(self, channel_id):
        # Primero buscamos si el canal existe y qué reglas de visibilidad tiene
        channel = request.env['im_livechat.channel'].sudo().browse(channel_id)
        if channel.exists():
            # Determinar si el usuario es público (no logueado)
            is_public = request.env.user._is_public()
            vis = channel.bot_visibility
            
            # Aplicar reglas de visibilidad
            if is_public and vis == 'authenticated':
                # El bot es solo para autenticados, y el usuario es público
                return {}
            
            if not is_public and vis == 'public':
                # El bot es solo para públicos, y el usuario está autenticado
                return {}

        # Si pasa las reglas de visibilidad, llamar al método original
        return super(VisibilidadBotLivechatController, self).livechat_init(channel_id)
