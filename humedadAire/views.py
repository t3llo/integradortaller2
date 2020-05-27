from django.shortcuts import render
from django.http import HttpResponse
import requests


def humedadAire(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        latitud = request.GET['latitude']
        longitud = request.GET['longitude']
        terreno = request.GET['terrain']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {"type": 'humedad', 'value': value, 'latitude': latitud, 'longitude': longitud, 'terrain' : terreno }
            #response = requests.post('http://127.0.0.1:8000/humedadAire/', args)
            response = requests.post('https://pi1-eafit-tello-back.azurewebsites.net/humedadAire/', args)
            # Convierte la respuesta en JSON
            humedadAire_json = response.json()

    # Realiza una petición GET al Web Services
    # response = requests.get('http://127.0.0.1:8000/humedadAire/')
    response = requests.get('https://pi1-eafit-tello-back.azurewebsites.net/humedadAire/')

    # Convierte la respuesta en JSON
    humedadAirelist = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "humedadAire/humedadAire.html", {'humedadAirelist': humedadAirelist})