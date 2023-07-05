import datetime
from django.http import HttpResponse
from django.template import Template, Context



def bienvenida(request):
    return HttpResponse("Bienvenido")

def categoriaedad(request, edad):
    if edad >= 18:
        return HttpResponse("Es mayor de edad")
    else:
        return HttpResponse("Es menor de edad")

def horaChile(request):
    hora = datetime.datetime.now()
    return HttpResponse(hora.strftime("%H:%M:%S"))

def contenidoHtml(request, nombre, edad):
    contenido = """
    <html>
        <head>
            <title>Mi primer vista</title>
        </head>
        <body>
            <h1>Mi primer vista</h1>
           <p> Nombre: {} / Edad: {}</p>
        </body>
    </html>
    """.format(nombre, edad)

    return HttpResponse(contenido)

def primera(request):

    plantillaexterna=open("cotizador/plantillas/primera.html")
    #cargar la plantilla
    template=Template(plantillaexterna.read())
    plantillaexterna.close()
    #creando el contexto
    contexto=Context()
    documento=template.render(contexto)
    return HttpResponse(documento)
def segunda(request):
    nombre="Alex"
    fecha=datetime.datetime.now
    lenguajes=["Python","Java","C#","C++"]
    plantillaexterna=open("cotizador/plantillas/parametros.html")
    #cargar la plantilla
    template=Template(plantillaexterna.read())
    plantillaexterna.close()
    #creando contexto
    contexto=Context({"nombre":nombre,"fecha":fecha, "lenguajes":lenguajes})
    documento=template.render(contexto)
    return HttpResponse(documento)