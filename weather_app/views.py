from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'kampala'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=607653a33a21bafbf41f4b4392c50e71'
    PARAMS = {'units': 'metric'}

    response = requests.get(url, params=PARAMS)

    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
    else:
        description = 'Error fetching data'
        icon = ''
        temp = ''

    day = datetime.date.today()

    return render(request, 'weatherapp/index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city':city})
