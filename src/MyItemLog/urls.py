"""MyItemLog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from pages.views import home_view
from pages.views import about_view
from pages.views import contact_view
from item.views import add_item_view
from item.views import delete_item_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('about/', about_view),
    path('add-item/', add_item_view),
    path('delete-item/', delete_item_view),
]

urlpatterns+= staticfiles_urlpatterns()

""" 
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
"""