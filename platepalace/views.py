from django.shortcuts import render
from django.http import HttpResponse

# HTTP REQUEST
def home(request): #cliente faz uma request ->  servidor retorna uma response
    return render(request, 'platepalace/home.html')
    # return  HTTP Response
