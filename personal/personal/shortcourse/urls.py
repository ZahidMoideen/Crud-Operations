"""personal URL Configuration

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
from django.contrib import admin
from django.urls import path
from shortcourse import views

urlpatterns = [
    path('',views.main,name='main'),
    path('add_page',views.add_page,name='add_page'),
    path('course_add',views.course_add,name='course_add'),
    path('update/<int:id>',views.update,name='update'),
    path('new_data',views.new_data,name='new_data'),
    path('delete_course/<int:id>',views.delete_course,name='delete_course'),
    path('account',views.account,name='account'),
    path('save_pass',views.save_pass,name='save_pass'),
    path('data',views.data,name='data'),
]
