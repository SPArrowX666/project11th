from django.shortcuts import render
from .models import Post 
import requests
def timeline(request):
    posts = Post.objects.select_related('author').order_by('-created_at')
    context = {
        'posts': posts,
    }

    return render(request, 'timeline.html', context)

# Create your views here.

def weather(request):
    # 1. 城市和坐标
    locations = {
        'Kanazawa': {'lat': 36.59, 'lon': 136.60},
        'Tokyo':    {'lat': 35.68, 'lon': 139.76},
        'Osaka':    {'lat': 34.69, 'lon': 135.50},
        'Sapporo':  {'lat': 43.06, 'lon': 141.35},
        'Naha':     {'lat': 26.21, 'lon': 127.68},
    }

    # 2. 默认城市（金泽）
    city_name = 'Kanazawa'
    if request.GET.get('city') in locations:
        city_name = request.GET.get('city')

    # 3. 取坐标
    lat = locations[city_name]['lat']
    lon = locations[city_name]['lon']

    # 4. API URL
    api_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )

    # 5. 调用 API
    response = requests.get(api_url)
    data = response.json()

    # 6. 传给 HTML
    context = {
        'city': city_name,
        'temperature': data['current_weather']['temperature'],
        'windspeed': data['current_weather']['windspeed'],
        'weathercode': data['current_weather']['weathercode'],
    }

    return render(request, 'weather.html', context)
