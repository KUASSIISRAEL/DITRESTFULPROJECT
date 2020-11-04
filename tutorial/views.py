from django.shortcuts import render
from rest_framework import generics 

from .serializers import OrderSerializer
from .serializers import GerantSerializer
from .serializers import MagasinSerializer
from .serializers import ArticleSerializer
from .serializers import InvoiceSerializer
from .serializers import CustomerSerializer

from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Order, Gerant, Magasin, Article, Invoice, Customer

# Create your views here.

class GerantList(generics.ListCreateAPIView):
    queryset         = Gerant.objects.all()
    serializer_class = GerantSerializer
    name             = 'gerants-list'

class GerantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Gerant.objects.all()
    serializer_class = GerantSerializer
    name             = 'gerant-details'

class MagasinList(generics.ListCreateAPIView):
    queryset         = Magasin.objects.all()
    serializer_class = MagasinSerializer
    name             = 'magasins-list'

class MagasinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Magasin.objects.all()
    serializer_class = MagasinSerializer
    name             = 'magasin-details'

class ArticleList(generics.ListCreateAPIView):
    queryset         = Article.objects.all()
    serializer_class = ArticleSerializer
    name             = 'articles-list'

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Article.objects.all()
    serializer_class = ArticleSerializer
    name             = 'article-details'

class CustomerList(generics.ListCreateAPIView):
    queryset         = Customer.objects.all()
    serializer_class = CustomerSerializer
    name             = 'customers-list'

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Customer.objects.all()
    serializer_class = CustomerSerializer
    name             = 'customer-details'

class OrderList(generics.ListCreateAPIView):
    queryset         = Order.objects.all()
    serializer_class = OrderSerializer
    name             = 'orders-list'

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Order.objects.all()
    serializer_class = OrderSerializer
    name             = 'order-details'

class InvoiceList(generics.ListCreateAPIView):
    queryset         = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    name             = 'invoices-list'

class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    name             = 'invoice-details'

class ApiRoot(generics.GenericAPIView): 
    name = 'api-root' 
    def get(self, request, *args, **kwargs): 
        return Response({ 
            'gerants'  : reverse(GerantList.name, request   = request),
            'magasins' : reverse(MagasinList.name, request  = request),
            'articles' : reverse(ArticleList.name, request  = request),
            'customers': reverse(CustomerList.name, request = request),
            'orders'   : reverse(OrderList.name, request    = request),
            'invoices' : reverse(InvoiceList.name, request  = request),
        }) 