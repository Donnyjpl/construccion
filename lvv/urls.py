from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

# URLs que no necesitan traducción
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # URLs para cambio de idioma
]

# URLs que serán traducidas (con prefijo de idioma)
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    prefix_default_language=True,  # No mostrar /es/ para español (idioma por defecto)
)

# Servir archivos estáticos y media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)