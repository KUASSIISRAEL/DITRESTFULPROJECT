from .models import Order
from .models import Gerant
from .models import Magasin
from .models import Article
from .models import Invoice
from .models import Customer
from rest_framework import serializers

class GerantSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='gerant-details', lookup_field='pk')
    
    class Meta:
        model  = Gerant
        fields = '__all__'

class MagasinSerializer(serializers.HyperlinkedModelSerializer):
    gerant = serializers.SlugRelatedField(queryset=Gerant.objects.all(), slug_field='pk')
    url = serializers.HyperlinkedIdentityField(view_name='magasin-details', lookup_field='pk')

    class Meta:
        model  = Magasin
        fields = '__all__'

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    magasin = serializers.SlugRelatedField(queryset=Magasin.objects.all(), slug_field='pk')
    url = serializers.HyperlinkedIdentityField(view_name='article-details', lookup_field='pk')

    class Meta:
        model  = Article
        fields = '__all__'
        deph   = 1

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='customer-details', lookup_field='pk')
    class Meta:
        model  = Customer
        fields = '__all__'

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    article  = ArticleSerializer()
    customer = CustomerSerializer()
    url = serializers.HyperlinkedIdentityField(view_name='order-details', lookup_field='pk')

    class Meta:
        model  = Order
        fields = '__all__'

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    order = OrderSerializer()
    url = serializers.HyperlinkedIdentityField(view_name='invoice-details', lookup_field='pk')
    
    class Meta:
        model  = Invoice
        fields = '__all__'