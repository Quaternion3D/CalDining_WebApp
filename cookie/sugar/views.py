import datetime

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.utils import timezone

from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://services.housing.berkeley.edu/FoodPro/dining/static/todaysentrees.asp"

# Create your views here.

#get todays food
def scrape(request):
    html = urlopen(BASE_URL).read()
    soup = BeautifulSoup(html, "lxml")

    def is_meal(tag):
        return tag.has_attr('width') and tag['width'] == '160' and tag.findAll("b")

    menus = soup.find_all(is_meal)
    for block in menus:
        time = block.find("b").get_text()
        loc = block.find("a")
        if loc:
            info = loc["href"]
            i = info.find("locationName") + 13
            location = info[i:]
            i = location.find("&")
            location = location[:i]
        for item in block.findAll("font"):
            food_name = item.contents[0]
	    	fod = Food.objects.filter(name=food_name)	
		    if not fod:
		        fod = Food(name=food_name, last_day_served=timezone.now())
				f.last_day_served = f.last_day_served.replace(day=f.last_day_served.day-1)
		        fod.save()
            else:
                fod.add_location(location, time)

#HOME
#landing page, login, about
def index(request):
	#add link to main

	return render_to_response('index.html')


def main(request):
	#scrape menu
		#add to database as a food item if it's not already there?
	#for all food items in database, populate list with radio buttons
	#
	return HttpResponse("main page, select foods & stuff")


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
		return HttpResponseRedirect('/sugar/loggedin')
	else:
		return HttpResponseRedirect('/sugar/invalid')	

def loggedin(request):
	return render_to_response('loggedin.html',
								{'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('loggedout.html')
