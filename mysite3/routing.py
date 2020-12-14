from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
import nuomiphp.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                nuomiphp.routing.websocket_urlpatterns
            )
        )
    ),
})