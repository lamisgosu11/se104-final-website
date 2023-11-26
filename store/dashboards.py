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

#Lớp biểu đồ đường đơn cho biểu đồ tuần cho đơn đặt hàng
class OrderWeekSingleLineChart(widgets.SingleLineChart):
    limit_to = 7 #giới hạn biểu đồ cho 7 ngày
    title = 'This Week Orders' #tiêu đề biểu đồ
    model = Order #mô hình dữ liệu được sử dụng, ở đây là Order
    width = widgets.LARGEST # Độ rộng của biểu đồ
    
    #biểu đồ đường đơn sử dụng thư viện Chartist
    #chứa các tùy chọn cấu hình cho thư viện Chartist, chẳng hạn như định dạng timestamp và các tùy chọn khác của biểu đồ.
    class Chartist:
            timestamp_options = {
            'year': 'numeric',
            'month': 'short',
            'day': 'short',
        }
            options = {
            'onlyInteger': True,
            'axisX': {
                'labelOffset': {
                    'x': -24,
                    'y': 0
                },
            },
            'chartPadding': {
                'top': 24,
                'right': 24,
            }
        }
    
    #Phương thức
    #Tạo danh sách nhãn cho trục x dựa trên ngày hiện tại và 7 ngày trước đó
    def labels(self):
        today = timezone.now().date()
        labels = [(today - datetime.timedelta(days=x)).strftime('%d/%m')
                  for x in range(self.limit_to)]
        return labels
    
    #Tạo dãy số liệu cho biểu đồ
    def series(self):
        series1 = []
        for label in self.labels:
            item = self.values[label]
            series1.append(item)
        series = []
        series.append(series1)
        return series
        
    #Trả về một từ điển các giá trị đơn đặt hàng cho mỗi ngày trong khoảng thời gian đã xác định
    def values(self):
        limit_to = self.limit_to * len(self.labels)
        queryset = self.get_queryset()
        queryset = queryset.extra({'order_day': 'order_day'}).values_list('order_day').annotate(count=Count('order_day')).order_by('-order_day')[:limit_to]
        values = defaultdict(lambda: 0)
        for order_day, count in queryset:
            order_day = order_day.strftime("%d-%m-%Y")
            day_month = '{0}/{1}'.format(*order_day.split('-'))
            values [day_month] = count
        return values


#Lớp biểu đồ đường đơn cho biểu đồ tháng cho đơn đặt hàng
class OrderMonthSingleLineChart(widgets.SingleLineChart):
    limit_to = 30 #giới hạn biểu đồ cho 30 ngày
    title = 'Commandes des Derniers 30 Jours' #tiêu đề biểu đồ
    model = Order #mô hình dữ liệu được sử dụng, ở đây là Order
    width = widgets.LARGEST # Độ rộng của biểu đồ

    #biểu đồ đường đơn sử dụng thư viện Chartist
    #chứa các tùy chọn cấu hình cho thư viện Chartist, chẳng hạn như định dạng timestamp và các tùy chọn khác của biểu đồ.
    class Chartist:
            timestamp_options = {
            'year': 'numeric',
            'month': 'short',
            'day': 'short',
        }
            options = {
            'onlyInteger': True,
            'axisX': {
                'labelOffset': {
                    'x': -24,
                    'y': 0
                },
            },
            'chartPadding': {
                'top': 24,
                'right': 24,
            }
        }
        
    #Phương thức
    #Tạo danh sách nhãn cho trục x dựa trên ngày hiện tại và 30 ngày trước đó
    def labels(self):
        today = timezone.now().date()
        labels = [(today - datetime.timedelta(days=x)).strftime('%d/%m')
                  for x in range(self.limit_to)]
        return labels

    #Tạo dãy số liệu cho biểu đồ   
    def series(self):
        series1 = []
        for label in self.labels:
            item = self.values[label]
            series1.append(item)
        series = []
        series.append(series1)
        return series
        
    #Trả về một từ điển các giá trị đơn đặt hàng cho mỗi ngày trong khoảng thời gian đã xác định
    def values(self):
        limit_to = self.limit_to * len(self.labels)
        queryset = self.get_queryset()
        queryset = queryset.extra({'order_day': 'order_day'}).values_list('order_day').annotate(count=Count('order_day')).order_by('-order_day')[:limit_to]
        values = defaultdict(lambda: 0)
        for order_day, count in queryset:
            order_day = order_day.strftime("%d-%m-%Y")
            day_month = '{0}/{1}'.format(*order_day.split('-'))
            values [day_month] = count
        return values


#Lớp biểu đồ đường đơn cho biểu đồ năm cho đơn đặt hàng
class OrderYearSingleLineChart(widgets.SingleLineChart):
    limit_to = 12 #giới hạng biểu đồ cho 12 tháng
    title = 'This Year Orders' #tiêu đồ của biểu đồ
    model = Order #mô hình dữ liệu được sử dụng, ở đây là Order
    width = widgets.LARGEST # Độ rộng của biểu đồ
    
    #biểu đồ đường đơn sử dụng thư viện Chartist
    class Chartist:
            timestamp_options = {
            'year': 'numeric',
            'month': 'short',
            'day': 'short',
        }
            options = {
            'onlyInteger': True,
            'axisX': {
                'labelOffset': {
                    'x': -24,
                    'y': 0
                },
            },
            'chartPadding': {
                'top': 24,
                'right': 24,
            }
        }

    #Phương thức
    #Tạo danh sách nhãn cho trục x có 12 tháng  
    def labels(self):
        # today = timezone.now().date()
        # labels = [(today - datetime.timedelta(days=x)).strftime('%d/%m')
        #           for x in range(self.limit_to)]
        labels = ['Jan', 'Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        return labels
    
    #Tạo dãy số liệu cho biểu đồ 
    def series(self):
        series1 = []
        for label in self.labels:
            item = self.values[label]
            series1.append(item)
        series = []
        series.append(series1)
        return series
        
    #Trả về một từ điển các giá trị đơn đặt hàng cho mỗi tháng trong khoảng thời gian đã xác định
    def values(self):
        limit_to = self.limit_to * len(self.labels)
        queryset = self.get_queryset()
        queryset = queryset.extra({'order_day': 'order_day'}).values_list('order_day').annotate(count=Count('order_day')).order_by('-order_day')[:limit_to]
        values = defaultdict(lambda: 0)
        for order_day, count in queryset:
            order_day = order_day.strftime("%b")
            # day_month = '{0}/{1}'.format(*order_day.split('-'))
            values [order_day] = count
        return values
    
#tạo biểu đồ tròn để hiển thị số lượng bình luận cho mỗi bài viết
class PostPieChart(widgets.SinglePieChart):
    limit_to = 2 #Giới hạn số lượng bài viết và bình luận (comments)
    title = 'Most Commented Articles' #Tiêu đề của biểu đồ
    model = Comment #Mô hình dữ liệu là Comment
    width = widgets.LARGE #Độ rộng của biểu đồ

    #Tạo danh sách nhãn cho các phần trong biểu đồ tròn
    def labels(self):
        labels = []
        for serie in self.series:
            item = self.values[serie]
            labels.append(item)
        return labels

    #Lấy danh sách các bài viết để hiển thị trong chú giải
    def legend(self):
        legend= list(Post.objects.values_list('title', flat=True))
        return legend

    #Lấy danh sách các bài viết để sử dụng trong biểu đồ   
    def series(self):
        series= list(Post.objects.values_list('id', flat=True))
        series = series
        return series

    #Trả về từ điển số lượng bình luận cho mỗi bài viết
    def values(self):
        limit_to = self.limit_to * len(self.legend)
        queryset = self.get_queryset()
        queryset = queryset.extra({'post': 'post_id'}).values_list('post_id').alias(count=Count('post_id')).annotate(count=Count('post_id')).order_by('count')[:limit_to]
        values = defaultdict(lambda: 0)
        for post, count in queryset:
            values [post] = count
        return values

#Hiển thị danh sách địa chỉ vận chuyển và thông tin liên quan
class UsersList(widgets.ItemList):
    title = 'Customers and Addresses' #Tiêu đề của danh sách
    model = ShippingAddress #Mô hình dữ liệu là ShippingAddress
    queryset = ShippingAddress.objects.all() #Truy vấn cơ sở dữ liệu để lấy danh sách địa chỉ vận chuyển
    list_display = ['customer','city', 'address'] # Các trường cần hiển thị trong danh sách
    list_display_links = ['user'] #Các trường liên kết đến chi tiết người dùng

    # Giới hạn itemlist là 30 mục
    limit_to = 30

    # Đặt chiều cao tối đa của Userlist là 300px và có thể cuộn
    height = 300


#Định nghĩa bảng điều khiển chứa các widgets đã được định nghĩa trước                        
class MyDashboard(Dashboard):
    #Thuộc tính widgets: Một tuple chứa các widgets sẽ xuất hiện trên dashboard
    widgets = (
        PostPieChart,
        UsersList,
        OrderWeekSingleLineChart,
        OrderMonthSingleLineChart,
        OrderYearSingleLineChart,
    )