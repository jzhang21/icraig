"""icraig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

#from craigslist.views import redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('craigslist.urls')),
  
    # - Unsure [From 'Updated Homepage']  -
    #url(r'^login/$', views.LoginView.as_view(), name='login'),
    #url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    #url(r'^auth/', include('social_django.urls', namespace='social')),
    # /-Unsure -
    path('accounts/', include('django.contrib.auth.urls')), #new
    #url(r^'login', auth_views.login, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  
    #url(r'^logout/$', 'django_social_app.views.logout'),
    #path('/redirect/', redirect_view)

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
