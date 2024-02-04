from django.http import HttpResponse
from django.template import Template, Context,loader
from miapp.models import *
import datetime, random 


def bienvenido1(request):
    return HttpResponse("Bienvenidos a la Comision 50200 - Clase  DJANGO")

def bienvenido2(request, nombre):
    respuesta = f"Bienvenido {nombre} a la Comision 50200 - Clase  DJANGO"
    return HttpResponse(respuesta)

def bienvenido3(request):
    hoy = datetime.datetime.now()
    respuesta = f"""
    <html>
    <h1>Bienvenidos al curso de Django!!</h1>
    <h2>Esta es la comision 50200</h2>
    <h3>Hoy es {hoy} </h3>
    </html>
    """
    return HttpResponse(respuesta)

def calcular_bruto(request, neto):
    neto = int(neto)
    respuesta = f"<html> <h1>Bruto de la factura es {neto*1.21} </h1> </html>"
    return HttpResponse(respuesta)

def bienvenido_template(request):
    hoy = datetime.datetime.now()
    nombre = "Amadeus"
    apellido = "Mozard"
    notas=[10,9,8,9]
    diccionario = {"nombre":nombre,"apellido":apellido, "autor":"Mario Oyarzabal", "fecha":hoy, "notas":notas}
    plantilla = loader.get_template('bienvenido.html')
    respuesta = plantilla.render(diccionario)
    return HttpResponse(respuesta)

def nuevo_curso(request):
    num_comision=random.randint(1,99999)
    srt_nombre ="Python"+str(num_comision)
    curso = Curso(nombre=srt_nombre,comision=num_comision)
    curso.save()
    documento = f"<html><h5> Se guardo {srt_nombre} y {num_comision} en la BD </h5></html>"
    return HttpResponse(documento)
