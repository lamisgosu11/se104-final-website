#file dashboards.py dùng để tạo bảng điều khiển (dashboards) cho admin - người bán

#import các module và lớp từ thư viện "controlcenter" để tạo Dashboard và các widget
from controlcenter import Dashboard, widgets

#import hàm "Count" từ Django để sử dụng trong truy vấn cơ sở dữ liệu
from django.db.models import Count

#import "defaultdict" để tạo dictionary có giá trị mặc định
from collections import defaultdict

#import timezone để xử lý thời gian và múi giờ
from django.utils import timezone

#import module "datetime để làm việc với các đối tượng ngày và thời gian
import datetime

#import các mô hình từ ứng dụng Django
from .models import Customer, Order, Post, Comment, ShippingAddress

#import mô hình User từ Django để làm việc với người dùng
from django.contrib.auth.models import User

