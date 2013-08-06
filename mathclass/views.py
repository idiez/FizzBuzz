from django.http import HttpResponse
from mathclass.fizzbuzz import *

def index_view(request):
	return HttpResponse(FizzBuzz().getFizzBuzz())