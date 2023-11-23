# Định nghĩa cấu trúc của một model Notification trong cơ sở dữ liệu
from django.db import migrations, models

# Định nghĩa lớp Migration, là cha cho tất cả các lớp migration trong dự án 
class Migration(migrations.Migration):

#   Đây là một migration khởi tạo, tức là sẽ thực hiện khi bạn chạy lệnh python manage.py migrate lần đầu tiên
    initial = True 
#   Không có dependency (phụ thuộc) nào được khai báo ở đây, nghĩa là migration này không phụ thuộc vào bất kỳ migration nào khác
    dependencies = [
    ]

#   Định nghĩa các thao tác cần thực hiện trong migration này. 
#   Trong trường hợp này, chỉ có một thao tác - tạo một model mới
    operations = [
#       Thực hiện việc tạo một model mới trong cơ sở dữ liệu
        migrations.CreateModel(
            name='Notification', # Tên của model sẽ là "Notification"

            # Định nghĩa các trường (fields) của model
            fields=[
                # Tạo một trường ID với kiểu dữ liệu là BigAutoField, tự động tăng, là trường chính (primary key) và không serialize (không chuyển đổi thành JSON) khi lấy dữ liệu từ cơ sở dữ liệu.
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # Tạo một trường có tên "count" với kiểu dữ liệu là IntegerField
                ('count', models.IntegerField()),
            ],
        ),
    ]

    # Một model có tên "Notification" sẽ được tạo trong cơ sở dữ liệu với hai trường là "id" và "count".
    # Trường "id" sẽ tự động tăng và là trường chính của model, còn trường "count" sẽ lưu giữ một giá trị kiểu số nguyên.