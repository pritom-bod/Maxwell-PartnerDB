import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PartnerConsumer(AsyncWebsocketConsumer):
    group_name = "partners"

    async def connect(self):
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def partner_event(self, event):
        # event["payload"] ক্লায়েন্টে পাঠান
        await self.send(text_data=json.dumps(event["payload"]))
