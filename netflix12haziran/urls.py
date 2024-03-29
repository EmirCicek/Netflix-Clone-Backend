"""
URL configuration for netflix12haziran project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from appMy.views import *
from appUser.views import *
from django.conf.urls import handler404, handler500
from appMy.views import *

# handler404 = error_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage, name='indexPage'),
    path('netflix', browseindexPage, name='browseindexPage'),
    path('profile', profilePage, name='profilePage'),
    path('profileDelete/<pid>', profileDelete, name='profileDelete'),
    path('profileLogin/<pid>', profileLogin, name='profileLogin'),
    path('category',categoryPage, name='categoryPage'),
    path('category/<kategori>',categoryPage, name='categoryPage'),
    # USER AUTH
    path('hesap', hesapPage, name='hesapPage'),
    path('login', loginPage, name='loginPage'),
    path('signup', registerPage, name='registerPage'),
    path('logoutUser', logoutUser, name='logoutUser'),

    # EMAIL MESSAGES
    path('emailmessagePage', emailmessagePage, name='emailmessagePage'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
