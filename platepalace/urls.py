from django.urls import path
from platepalace.views import home

# dominio.com/platepalace/
urlpatterns = [
    path('', home ), # Home
   
]
