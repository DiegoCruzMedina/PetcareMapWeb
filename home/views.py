from django.shortcuts import render
from user_agents import parse  # Esta línea debe estar presente
from django.http import HttpResponse



# Create your views here.
def index(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    
    # El enlace de descarga de la APK
    apk_url = 'https://github.com/JhonnyBoy12/ExamenTransversal/raw/main/app-debug.apk' 
    
    # Detectamos si el dispositivo es móvil
    if user_agent.is_mobile:
        # Si es móvil, le pasamos el enlace como un QR
        return render(request, 'home/index.html', {'apk_url': apk_url, 'is_mobile': True})
    else:
        # Si es escritorio, le pasamos el enlace directo
        return render(request, 'home/index.html', {'apk_url': apk_url, 'is_mobile': False})