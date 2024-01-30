"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chatapp.routing # in app chatapp routing.py file


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings") # tells Django which settings module to use when starting the ASGI app, i.e. mysite.settings module (aka settings.py)

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chatapp.routing.websocket_urlpatterns
        )
    )
})
# above, ProtocolTypeRouter is a router provided by Channels that allows you to route different types of protocol to diff apps, i.e. 'http' requests to the default Django WSGI app, and 'websocket' requests to a custom routing config for handling WebSocket connections

# for 'http' requests it uses the get_asgi_application() to get the default Django WSGI app (same app used for handling traditional synchronous HTTP requests)
# for 'websocket' connections it used the AuthMiddlewareStack to add authentication support, then inside that it includes a URLRouter, that is configured with the WebSocket URL patterns defined in chatapp.routing.websockets_urlpatterns (i.e. routing.py inside your chatapp app)

