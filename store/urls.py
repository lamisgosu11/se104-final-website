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
    path('blog_article/<str:slug>/', views.blog_article, name="blog_article"),
    path('contact/', views.contact, name="contact"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', viewslogoutUser, name="logout"),
]