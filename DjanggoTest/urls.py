"""DjanggoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from . import view
from django.conf.urls import *
from . import view, testdb, search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.index),
    url(r'^he$', view.hello),
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^testdb1$', testdb.testdb3),
    url(r'^testdb2$', testdb.testdb2),
    url(r'^testdb3$', testdb.testdb1),

    url(r'^queryContact', testdb.queryContact),
    url(r'^search-form$', search.search_form),
    url(r'^search-get$', search.search_get),
    url(r'^search-post$', search.search_post),
    url(r'^search-request$', search.search_request),
]