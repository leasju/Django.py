from django.urls import path
from platepalace.views import home, contato, sobre

# dominio.com/platepalace/
urlpatterns = [
    path('', home ), # Home
    path('sobre/', sobre), # /sobre/
    path('contato/', contato) # /contato/
]
