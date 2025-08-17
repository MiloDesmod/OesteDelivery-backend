# core/urls.py
from django.contrib import admin
from django.urls import path, include
# --- Importaciones necesarias para servir archivos ---
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs de nuestras apps
    path('api/', include('locales.urls')),
    path('api/', include('ordenes.urls')),
    path('api/usuarios/', include('usuarios.urls')),
    
    # URLs de autenticación
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/', include('allauth.urls')),
]

# --- BLOQUE DE CÓDIGO CLAVE ---
# Esta es la instrucción que le dice a Django cómo servir las imágenes
# que subimos desde el admin durante el desarrollo.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)