"""
URL configuration for EVA4_FINAL project.

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
from django.urls import path, include
from django.views.generic.base import TemplateView
from reservasAPP.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("dashboard/", Dashboard, name="dashboard"),
    path("estados/", Estados, name="estados"),
    path("reservas/", Reservas, name="reservas"),
    path("insertReserva/", insertReserva, name="insertReserva"),
    path("editarReserva/<int:id>", editarReserva, name="editarReserva"),
    path("dropReserva/<int:id>", dropReserva, name="dropReserva"),
    path('api-auth/', include('rest_framework.urls')),
    path("reservasAPI/", vistaReservaAPI, name="vistaReservaAPI"),
    path("vistaReservaApi2/", vistaReservaApi2, name="vistaReservaApi2"),
    path("vistaReservaApi2/<int:pk>/", user_detail_api_view, name='ReservaAPIDetailView')
]
