from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name='index'),

    #Search for different images bases on category 
    path('search/', views.search_results, name='search_results'),

    #view location.html
    path('location/', views.category, name='location'),

    #view category.html
    path('category', views.category, name='category'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)