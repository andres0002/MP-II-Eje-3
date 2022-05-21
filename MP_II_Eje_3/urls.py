"""MP_II_Eje_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ListUsers.as_view(), name="list_user"),
    path('adduser/', views.AddUser.as_view(), name="add_user"),
    path('visualizeuser/<slug:cedula>', views.VisualizeUser.as_view(), name="visualize_user"),
    path('updateuser/<slug:cedula>', views.UpdateUser.as_view(), name="update_user"),
    path('deleteuser/<slug:cedula>', views.DeleteUser.as_view(), name="delete_user"),
]
