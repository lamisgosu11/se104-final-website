# Thêm một trường mới có tên 'active' vào model 'notification' trong ứng dụng 'admin_notification', với giá trị mặc định là True

from django.db import migrations, models

# Định nghĩ lớp Migration, là lớp cha của các migration khác trong dự án
class Migration(migrations.Migration):

#   Đặt phụ thuộc của migration này là migration "001_initial" nằm trong admin_notification.
#   Tức là migration "001_initial" phải thực hiện thành công thì migration này mới bắt đầu thực hiện.
    dependencies = [
        ('admin_notification', '0001_initial'),
    ]

#   Định nghĩa các thao tác trong migration này.
    operations = [
        #   Thao tác: AddFeild - thêm một trường mới vào model
        migrations.AddField(
            model_name='notification',  # Model có tên là "notification"
            name='active',  # Đặt tên trường mới là "active"
            field=models.BooleanField(default=True),    # Đặt kiểu dữ liệu cho trường là boolean, giá trị mặc định là "True"
        ),
    ]
