from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post-land/', views.post_land, name='post_land'), # Indha 'name' dhaan important
    path('land/<int:land_id>/', views.land_detail, name='land_detail'),

    path('add-to-cart/<int:land_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),

]