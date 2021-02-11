from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'core/index.html')

def resume(request):
	context = {
		"title": "Resume"
	}
	return render(request, 'core/resume.html', context)
