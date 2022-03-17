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
    DescriptionView,
    ProjectView,
    EducationView,
    ProspectView,
    VitaView,
    ExerienceView,
    LanguageView,
    MissionView,
    EducationVitaView,
    ExperienceVitaView,
    ExperienceFrameView,
    ExperienceLangView,
    AppicationView,
    get_profile,
    login_user,
    register_user,
    )

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'frameworks', FrameworkView, 'framework')
router.register(r'jobtypes', JobtypeView, 'jobtype')
router.register(r'descriptions', DescriptionView, 'description')
router.register(r'projects', ProjectView, 'project')
router.register(r'educations', EducationView, 'education')
router.register(r'educationvitas', EducationVitaView, 'education_vita')
router.register(r'prospects', ProspectView, 'prospect')
router.register(r'vitas', VitaView, 'vita')
router.register(r'experienceframes', ExperienceFrameView, 'experience_frame')
router.register(r'experiencevitas', ExperienceVitaView, 'experience_vita')
router.register(r'experiencelangs', ExperienceLangView, 'experience_lang')
router.register(r'experiences', ExerienceView, 'experience')
router.register(r'languages', LanguageView, 'language')
router.register(r'missions', MissionView, 'mission')
router.register(r'applicant', AppicationView, 'applicant')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('profile', get_profile),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
