from ast import Or
from http.client import HTTPResponse
from unicodedata import category
from django.shortcuts import HttpResponse
from itertools import product
from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import json
import datetime
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from store.forms import CommentForm, CreateUserForm
from store.models import *

# need to create forms and models

# Create your views here.

# Store view
# case 1: user đã login -> lấy order của user đó -> lấy tất cả các item trong order đó -> lấy cartItems từ order đó
# case 2: user chưa login -> tạo order mới -> để cart items = 0 và ko có mặt hàng nào trong order đó

# -> Sau đó, lấy tất cả các sản phẩm từ cơ sở dữ liệu và trả về một trang HTML với thông tin về các sản phẩm và số lượng mặt hàng trong giỏ hàng.


def store(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

# home view tương tự như store view nhưng chỉ lấy 4 sản phẩm đầu tiên
# và 3 bài viết đầu tiên -> sau đó trả về một trang HTML với thông tin về các sản phẩm và số lượng mặt hàng trong giỏ hàng.


def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    products = Product.objects.all()[:4]
    articles = Post.objects.all()[:3]
    context = {'articles': articles,
               'products': products, 'cartItems': cartItems}
    return render(request, 'store/home.html', context)

# product view xử lý yêu cầu của người dùng để xem chi tiết sản phẩm
# -> sau đó trả về một trang HTML với thông tin về sản phẩm và các sản phẩm liên quan, sử dụng slug để xác định sản phẩm cụ thể và
# lấy các sản phẩm liên quan từ cùng một danh mục.
# -> nếu sản phẩm không tồn tại, trả về một trang 404


def product(request, slug):
    # te3 product detaillé
    print('Product slug', slug)
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category)[:4]
    context = {'product': product, 'related_products': related_products}
    return render(request, 'store/product.html', context)

# blog_article view xử lý yêu cầu của người dùng để xem chi tiết bài viết
# -> sau đó trả về một trang HTML với thông tin về bài viết và các bài viết liên quan, sử dụng slug để xác định bài viết cụ thể và
# lấy các bài viết liên quan từ cùng một danh mục.
# -> nếu bài viết không tồn tại, trả về một trang 404


def blog_article(request, slug):
    print('post slug', slug)
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST, instance=post)
    if (request.method == 'POST'):
        if (form.is_valid):
            body = form.cleaned_data['body']
            print(body)
            c = Comment(post=post, body=body, date_commented=datetime.now())
            c.save()
            return redirect('store/blog_article.html')
        else:
            print('form is invalid')

    context = {'post': post, 'form': form}
    return render(request, 'store/blog_article.html', context)

# blog view trả về một trang HTML với tất cả các bài viết


def blog(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'store/blog.html', context)

# contact view trả về một trang HTML với thông tin liên hệ


def contact(request):
    return render(request, 'store/contact.html')

# cart view trả về một trang HTML với thông tin về các sản phẩm trong giỏ hàng (mặt hàng, đơn hàng, số lượng)


def cart(request):
    # cart o payement wkol maysyro ken b customer is already connected sinn yatl3o 0
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

# checkout view
# -> nếu người dùng đã đăng nhập, lấy đơn hàng của người dùng đó và số lượng mặt hàng trong giỏ hàng
# -> nếu người dùng chưa đăng nhập, trả về một trang HTML với các sản phẩm trong giỏ hàng (mặt hàng, đơn hàng, số lượng) là 0


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)
