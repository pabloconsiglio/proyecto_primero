from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template

def hola(request):
    return HttpResponse('<h2>Buenas clase</h2>')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'La hora y fecha actual es {fecha_actual}')

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años es: {fecha}')

def mi_template(request):
    
    cargar_archivo = open(r'C:\Users\Pablo\Desktop\primer_proyecto\proyecto_nuevo\templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)