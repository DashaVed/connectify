from rest_framework.generics import ListAPIView

from chat.models import Chat
from chat.serializers import ChatSerializer


class ChatView(ListAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        room = self.request.query_params.get('room', None)
        return Chat.objects.filter(room=room)
