from django.shortcuts import HttpResponse

#create a view called index that takes one argument (request)
#and returns an HttpResponse

def index(request):
	return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")
	
def about(request):
	return HttpResponse("Rango says: Here is the about page. <a href='/rango/'>Index</a>")