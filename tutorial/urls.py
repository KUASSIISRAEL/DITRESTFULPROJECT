from . import views
from django.urls import path

urlpatterns = [
    path('gerants/',  
        views.GerantList.as_view(),  
        name=views.GerantList.name),

    path('gerant/<int:pk>/',  
        views.GerantDetail.as_view(), 
        name=views.GerantDetail.name), 

    path('magasins/',  
        views.MagasinList.as_view(),  
        name=views.MagasinList.name),

    path('magasin/<int:pk>/',  
        views.MagasinDetail.as_view(), 
        name=views.MagasinDetail.name),

    path('articles/',  
        views.MagasinList.as_view(),  
        name=views.MagasinList.name),

    path('article/<int:pk>/',  
        views.ArticleList.as_view(), 
        name=views.ArticleDetail.name),

    path('customers/',  
        views.MagasinList.as_view(),  
        name=views.MagasinList.name),

    path('customer/<int:pk>/',  
        views.CustomerList.as_view(), 
        name=views.CustomerDetail.name), 

    path('orders/',  
        views.MagasinList.as_view(),  
        name=views.MagasinList.name),

    path('order/<int:pk>/',  
        views.OrderList.as_view(), 
        name=views.OrderDetail.name),

    path('invoices/',  
        views.MagasinList.as_view(),  
        name=views.MagasinList.name),

    path('invoice/<int:pk>/',  
        views.InvoiceList.as_view(), 
        name=views.InvoiceDetail.name),
]
