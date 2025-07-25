from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework import viewsets

def pagina_inicial(request):
    return render(request, 'index.html')

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
