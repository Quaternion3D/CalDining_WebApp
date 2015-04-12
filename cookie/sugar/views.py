from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

# Create your views here.

#get todays food
def scrape(request):



#HOME
#landing page, login, about
def index(request):
	#add link to main

	return HttpResponse("THIS IS THE HOME PAGE")


def main(request):
	#scrape menu
		#add to database as a food item if it's not already there?
	#for all food items in database, populate list with radio buttons
	#
	return HttpResponse("main page, select foods & stuff")


'''
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c);

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/loggedin')
	else
		return HttpResponseRedirect('/invalid')	

def loggedin(request):
	return render_to_response('loggedin.html',
								{'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

'''