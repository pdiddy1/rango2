from django.shortcuts import HttpResponse, render_to_response
from django.template import RequestContext


#create a view called index that takes one argument (request)
#and returns an HttpResponse

def index(request):
	#request the context of the request
	#the context contains info such as the client's machine details, for example
	context = RequestContext(request)
	
	#construct a dictionary to pass to the template engine as its context.
	#note the key boldmessage is the same as the {{bold message}} in the template
	context_dict = {'boldmessage': "I am bold font from the context."}
	
	#return a rendered response to send to the client. use the shortcut function
	#note that the first parameter is the template we wish to use.
	return render_to_response('rango/index.html', context_dict, context)
	
def about(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "I am even bolder font from the context.'"}
	return render_to_response('rango/about.html', context_dict, context)
	
	#	return HttpResponse("Rango says: Here is the about page. <a href='/rango/'>Index</a>")