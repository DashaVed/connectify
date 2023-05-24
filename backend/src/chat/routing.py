from django.urls import path

from chat.consumers import MainConsumer

websocket_urlpatterns = [path("ws/server/<str:room>/", MainConsumer.as_asgi())]