from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
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
