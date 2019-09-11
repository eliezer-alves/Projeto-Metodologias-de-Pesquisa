"""sospet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from core.views import login_user, submit_login, logout_user, index, list_all_pets, list_user_pets, pet_detail, pet_register, set_pet, pet_delete
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns #para as imagens . Não sei porque
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_user, name="login"),
    path('login/submit', submit_login),
    path('login/', logout_user, name="logout"),
    path('', RedirectView.as_view(url='pet/all/')),
    path('pet/all/', list_all_pets, name="all_pets"),
    path('pet/user/', list_user_pets, name="user_pets"),
    path('pet/detail/<id>/', pet_detail, name="pet_detail"),
    path('pet/register/', pet_register, name="pet_register"),
    path('pet/delete/<id>', pet_delete, name="pet_delete"),
    path('pet/register/submit', set_pet),
    path('index/', index, name="index"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)