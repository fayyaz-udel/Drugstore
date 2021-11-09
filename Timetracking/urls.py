"""DrugStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.employee_dashboard, name='employee_dashboard'),
    path("user", login_required(views.UserList.as_view()), name="userList"),
    path('log_create', views.log_create_request, name="log_create"),
    path('<id>/log_finish', views.log_finish_request, name="log_finish"),
    path('<id>/log_pay', views.log_pay_request, name="log_pay"),
    path('<id>/log_delete', views.log_delete_request, name="log_delete"),
    path('<id>/user_delete', views.user_delete_request, name="user_delete"),
    path("logout", views.logout_request, name="logout"),
    path("register", views.register_request, name="register"),
    path("logs", login_required(views.LogList.as_view()), name="report"),

]