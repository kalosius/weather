from django.shortcuts import render
import requests
import datetime

def index(request):
    # Get the 'city' from the request POST data or use a default value ('kampala')
    city = request.POST.get('city', 'kampala')

    # OpenWeatherMap API
    weather_api_key = '607653a33a21bafbf41f4b4392c50e71'
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}'
    weather_params = {'units': 'metric'}

    # Google Custom Search API for images
    search_engine_id = '265e48dc74c4845ca'
    query = f'{city} 1920x1080'
    page = 1
    start = (page - 1) * 10 + 1
    search_type = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={weather_api_key}&cx={search_engine_id}&q={query}&start={start}&searchType={search_type}&imgSize=xlarge"

    # Initialize variables for weather data
    description = ''
    icon = ''
    temp = ''

    # Fetch weather data from OpenWeatherMap
    weather_response = requests.get(weather_url, params=weather_params)

    if weather_response.status_code == 200:
        weather_data = weather_response.json()
        weather_info = weather_data.get('weather', [])
        if weather_info:
            description = weather_info[0].get('description', 'N/A')
            icon = weather_info[0].get('icon', '')
            temp = weather_data['main'].get('temp', 'N/A')

    # Fetch image data from Google Custom Search
    city_data = requests.get(city_url).json()
    search_items = city_data.get("items")
    image_url = search_items[0]['link'] if search_items else ''

    # Get the current date
    day = datetime.date.today()

    # Render the template with the collected data
    context = {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city,
        'image_url': image_url,
    }

    return render(request, 'weatherapp/index.html', context)
