from django.shortcuts import render

def prueba(request):
    return render(request, 'App_analisis_datos/index.html')