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
from pages.views import home_search
from pages.views import profile_view
from item.views import add_item_view
from item.views import delete_item_view
from item.views import delete_all_item_view
from item.views import edit_item_view
from item.views import entry_download
from register.views import register
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.conf import settings
from django.urls import include
from django.views.static import serve
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home_view, name='home'),
    path('search/', home_search, name='search'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('add-item/', add_item_view, name='add-item'),
    path('delete-item/<int:id>', delete_item_view, name='delete-item'),
    path('edit-item/<int:id>', edit_item_view, name='edit-item'),
    path('delete-all/', delete_all_item_view, name='delete-all'),
    path('item-download/', entry_download, name='item-download'),
    path('', include("django.contrib.auth.urls"), name="login"),
    path("register/", register, name="register"),
    path('profile/', profile_view, name="profile"),
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