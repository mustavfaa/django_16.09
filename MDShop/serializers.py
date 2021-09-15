from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from .models import smartphone
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import User


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username")

               
class MDShopListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = smartphone
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
   
    class Meta:
        model = Customer
        fields = '__all__'


class MDShopSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = smartphone
        fields = '__all__'


class MDShopCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = smartphone
        fields = '__all__'


class CreateCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class CustomerLikeSerializer(serializers.ModelSerializer):
    likeNEW=MDShopSerializer( read_only=True)

    class Meta:
        model = CustomerLike
        fields = ("id", "likeNEW", "likeCustomer","created_at")


class CustomerCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerLike
        fields = '__all__'


class CustomerAddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomerAddress
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = smartphone
        fields = '__all__'
    
    
class OrderCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = order
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    smartphone=ShopSerializer(read_only=True,many=True)
    
    class Meta:
        model = order
        fields = '__all__'   