"""CV_ables URL Configuration

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
from rest_framework import routers
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from CV_ables_api.views import (
    FrameworkView,
    JobtypeView,
    get_profile,
    get_experience_list,
    get_discription_list,
    get_education_list,
    get_language_list,
    get_mission_list,
    login_user,
    register_user,
    )

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'frameworks', FrameworkView, 'framework')
router.register(r'jobtypes', JobtypeView, 'jobtype')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('profile', get_profile),
    path('experiences', get_experience_list),
    path('descriptions', get_discription_list),
    path('educations', get_education_list),
    path('languages', get_language_list),
    path('missions', get_mission_list),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
