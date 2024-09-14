from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls), # caminho nunca começa com /
    path('', include('platepalace.urls')), # include inclui as urls do platepalace aqui
 
]
