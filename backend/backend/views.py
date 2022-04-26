from django.http import HttpResponse
from django.views import View
from PIL import Image
from django.http import FileResponse

class Viewer(View):
	@staticmethod
	def get(request):
		# return HttpResponse('aiueo')
		img = open(r'backend\static\aaa.png', 'rb')
		response = FileResponse(img)
		return response
