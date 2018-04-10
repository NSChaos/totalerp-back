"""totalerp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from custom_auth.views import SignIn, SignOut, Profile
# from core.views import Core, Component

urlpatterns = [
    url(r'^$', RedirectView.as_view(
        url='admin/',
        permanent=True
    )),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include([
        url(r'^auth/', include(
            'rest_framework.urls',
            namespace='rest_framework')),
        url(r'^signin/$',
            SignIn.as_view(),
            name='sign_in'),
        url(r'^signout/$',
            SignOut.as_view(),
            name='sign_out'),
        url(r'^profile/$',
            Profile.as_view(),
            name='profile'),
        # url(r'^core/$',
        #     Core.as_view(),
        #     name='core')
        # url(r'^component/$',
        #     Component.as_view(),
        #     name='component')
    ]))
]

