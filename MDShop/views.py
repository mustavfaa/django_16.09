from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from .models import smartphone,Genre
from .serializers import MDShopListSerializer,MDShopSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination 
from django_filters.rest_framework import DjangoFilterBackend
from .service import  ShoppFilter
from django_filters import rest_framework as filters
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.generics import  RetrieveUpdateDestroyAPIView
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status


class CustomerLikeView(APIView):    
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request):
        queryset =CustomerLike.objects.filter(likeCustomer__user=self.request.user).distinct()
        serializer=CustomerLikeSerializer(queryset, many=True)
        return Response(serializer.data)


class CustomerLikeCreateView(generics.CreateAPIView):
    queryset = CustomerLike.objects.all()
    serializer_class = CustomerCreateSerializer
   

class CustomerRetrieveView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        queryset = Customer.objects.filter(Q(user=request.user))
        serializer = CustomerSerializer(queryset, many=True)
        return Response({"data": serializer.data})


class CustomerUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateCustomerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)
  

class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

    
class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ShoppFilter(filters.FilterSet):
    price = filters.RangeFilter()
    genres = CharFilterInFilter(field_name='genres__name', lookup_expr='in')
    title = SearchFilter()
    
    class Meta:
        model = smartphone
        fields = ['price','genres','title']


class MDShopListView(generics.ListAPIView):
    queryset = smartphone.objects.all()
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ['title']
    filterset_class = ShoppFilter
    
    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset()).distinct()
        serializer=MDShopListSerializer(queryset,many=True)
        return Response(serializer.data)


class MDShopView(APIView):

	def get(self,request,id):
		mds=smartphone.objects.get(id=id)
		serializer=MDShopSerializer(mds)
		
		return Response(serializer.data)


@api_view(['DELETE'])
def tutorial_detail(request, id):    
    tutorial = CustomerLike.objects.get(id=id) 
    if request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'})


@api_view(['PUT'])
def tutoria(request, id):
    tutorial = Customer.objects.get(id=id) 
    if request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = CreateCustomerSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse({'message': 'Tutorial was deleted ereerrrror!'})


class CustomerAddressCreateView(generics.CreateAPIView):
    queryset          =  CustomerAddress.objects.all()
    serializer_class  =  CustomerAddressSerializer


class CustomerAddressView(APIView):    
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request):
        queryset =CustomerAddress.objects.filter(addressCustomer__user=self.request.user)
        serializer=CustomerAddressSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def PutCustomerView(request, id):
    tutorial = CustomerAddress.objects.get(id=id)  
    if request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = CustomerAddressSerializer(tutorial, data=tutorial_data)
        permission_classes = (permissions.IsAuthenticated,) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse({'message': 'Tutorial was deleted ereerrrror!'})


@api_view(['DELETE'])
def DeleteCustomerAddressView(request, id):
    tutorial = CustomerAddress.objects.get(id=id)  
    if request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'})

        
class OrderCreateView(generics.CreateAPIView):
    queryset = order.objects.all()
    serializer_class = OrderCreateSerializer


class OrderView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request):
        queryset =order.objects.filter(orderCustomer__user=self.request.user)
        serializer=OrderSerializer(queryset, many=True)
        return Response(serializer.data)