from django.shortcuts import render

def home(request):
	
	import json
	import requests

	api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Delhi&units=metric&appid=cd4415a99345841edbb9040348e3f2d6")


	try:
		api = json.loads(api_request.content)

	except Exception as e:
		api = "Error"

	return render(request,'home.html',{'api':api})


def about(request):
	return render(request,'about.html',{})
