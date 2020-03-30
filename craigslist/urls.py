from django.urls import path, include

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    #path('create_listing/', views.CreateListingView.as_view(success_url="/create_listing/"), name='create_listing'),
    path('create_listing/', views.create_listing, name='create_listing'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('s/', views.ItemList.as_view(), name='itemlist'),
    path('locations/', views.LocationView.as_view(), name='locations'),

    

    path('m/messages/', include('django_messages.urls')),
    path('profile/<str:usr>/', views.ProfileView.as_view(), name='profile'), # Path for viewing own profile
    path('<str:user>/<int:id>/', views.ListingView.as_view(), name='listing'), # Path for viewing individual listings. YYYYMMDDHHMMSS
    path('<str:user>/<int:id>/mark_sold/', views.mark_sold, name='mark_sold'),
    path('<str:usr>/', views.ForeignProfileView.as_view(), name='foreignprofile'), # Path for viewing other user page


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
