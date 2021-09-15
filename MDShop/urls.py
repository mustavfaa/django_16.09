
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

	path("mds/", views.MDShopListView.as_view(), name='posts_view'),
	path("mds/<int:id>/", views.MDShopView.as_view()),
	path('auth/', include('djoser.urls')),
	path('auth/token/', obtain_auth_token, name='token'),
	path('customers/', views.CustomerRetrieveView.as_view()),
	path('customer/update/<int:id>', views.CustomerUpdateView.as_view()),
    path('customers/all', views.CustomerListView.as_view()),
    path('customers/create/<int:id>', views.CustomerCreateView.as_view()),
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("customer/like/", views.CustomerLikeView.as_view()),
    path("customer/like/create", views.CustomerLikeCreateView.as_view()),
    path("customer/like/delete/<int:id>", views.tutorial_detail),
    path("customer/address/create", views.CustomerAddressCreateView.as_view()),
    path("customer/address/", views.CustomerAddressView.as_view()),
    path('address/update/<int:id>', views.PutCustomerView),
    path("customer/address/delete/<int:id>", views.DeleteCustomerAddressView),
    path("customer/order/create", views.OrderCreateView.as_view()),
    path("customer/order", views.OrderView.as_view()),   
    
 ]