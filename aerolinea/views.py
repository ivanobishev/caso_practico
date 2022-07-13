from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Flight
import aiohttp, asyncio, requests, time

# Create your views here.
async def get_data(session, url):
    async with session.get(url) as res:
        api_data = await res.json()
        return api_data

async def inicio(request):

    starting_time = time.time()
    actions = []
    api_data = []

    async with aiohttp.ClientSession() as session:
        for num in range(1, 51):
            # Flights from the API.
            #url = f"http://api.aviationstack.com/v1/flights/{num}?access_key=b27a6f5d130a5406ea57f56f3f7be4cf"
            url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            actions.append(asyncio.ensure_future(get_data(session, url)))
        pokemon_res = await asyncio.gather(*actions)
        for data in pokemon_res:
            api_data.append(data)

    count = len(api_data)
    total_time = time.time() - starting_time

    # Flights from our local database.
    #flights = Flight.objects.all()

    return render(
        request,
        "inicio.html",
        {"data": api_data, "count": count, "time": total_time}
    )

# Very low.
'''async def vuelos(request):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://pokeapi.co/api/v2/pokemon/1") as res:
            data = await res.json()
            print(data)

    return render(
        request,
        "vuelos.html",
        {"data": data}
    )'''

# Low.
'''def vuelos(request):

    starting_time = time.time()
    pokemon_data = []

    for num in range(1, 101):
        url = f"https://pokeapi.co/api/v2/pokemon/{num}"
        res = requests.get(url)
        pokemon = res.json()
        pokemon_data.append(pokemon["name"])

    count = len(pokemon_data)
    total_time = time.time() - starting_time

    return render(
        request,
        "vuelos.html",
        {"data": pokemon_data, "count": count, "time": total_time}
    )'''

# Normal.
'''async def vuelos(request):

    starting_time = time.time()
    pokemon_data = []

    async with aiohttp.ClientSession() as session:
        for num in range(1, 101):
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            async with session.get(pokemon_url) as res:
                pokemon = await res.json()
                pokemon_data.append(pokemon["name"])

    count = len(pokemon_data)
    total_time = time.time() - starting_time

    return render(
        request,
        "vuelos.html",
        {"data": pokemon_data, "count": count, "time": total_time}
    )'''
