"""
URL configuration for garnilo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import index, rota_list, vzvod_list, person_detail, change_position

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path("rota/<int:rota_id>/", rota_list, name='rota_list'),
    path("rota/<int:rota_id>/vzvod/<int:vzvod_id>", vzvod_list, name='vzvod_list'),
    path("person/<int:person_id>/", person_detail, name='person_detail'),
    path("change/position/<int:person_id>/", change_position, name='change_position'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)