from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import About
# Create your views here.
def about_test(request):
    return HttpResponse("return this string")
def about_home(request):
	about =get_object_or_404(About,pk=1)
	return render(request, 'sitepages/about.html', {'about':about})
