from channels.generic.websocket import WebsocketConsumer
import json

from main.models import Code


class ClickerConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()

	def disconnect(self, close_code):
		pass

	def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['addAmount']

		if Code.objects.count() == 0:
			code = Code.objects.create()
		# You can do something here as this should be the first person
		else:
			code = Code.objects.first()
		# TODO: use addAmount instead
		code.clicks = code.clicks + int(message)
		code.save()
		print(code.clicks)

		self.send(text_data=json.dumps({
			'clicks': code.clicks
		}))
