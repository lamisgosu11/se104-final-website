# Thay đổi giá trị mặc định của trường 'count' trong model 'notification' thành 0

from django.db import migrations, models

# Định nghĩa một lớp Migration
class Migration(migrations.Migration):

#   Migration này phụ thuộc vào migration "0002_notification_active"
    dependencies = [
        ('admin_notification', '0002_notification_active'),
    ]

#   Định nghĩa các thao tác trong migration này
    operations = [
        # Thao tác: AlterField - Thay đổi thông tin của trường trong model.
        migrations.AlterField(
            model_name='notification',  # Tên model: notification
            name='count',   # Tên trường cần thay đổi: count
            field=models.IntegerField(default=0),   # Giá trị mặc định của trường được đặt là 0
        ),
    ]