from django.contrib import admin
from django.urls import path
from cotizador.views import bienvenida, categoriaedad, horaChile, contenidoHtml,primera,segunda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida),
    path('edades/<int:edad>/', categoriaedad),
    path('horaChile/', horaChile),
    path('contenido/<str:nombre>/<int:edad>/', contenidoHtml),
    path('primera/', primera),
    path('segunda/', segunda),
]
