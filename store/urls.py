from django.urls import path

from . import views

urlpatterns = [
    path('', views.store, name = "store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('home/', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('product/<str:slug>/', views.product, name="product"),
    
]