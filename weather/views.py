import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    if(request.method == "POST"):
        form = CityForm(request.POST)
        form.save()

    appid = 'b77c3611b1e29721a9d2f603c70d53c8'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid


    form = CityForm()

    cities = City.objects.all()

    allcities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
			'city': city.name,
			'temperature': res["main"]["temp"],
			'icon': res['weather'][0]['icon']
		}

        allcities.append(city_info)

    context = {'all_info': allcities, 'form': form}
    return render(request, 'weather/index.html', context)


def info(request):
    return render(request, 'weather/info.html')