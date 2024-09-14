from django.shortcuts import render
from django.http import HttpResponse

# HTTP REQUEST
def home(request): #cliente faz uma request ->  servidor retorna uma response
    return HttpResponse('HOME')
    # return  HTTP Response
    
def contato(request): 
    return HttpResponse('CONTATO')

def sobre(request): 
    return HttpResponse('SOBRE')

   