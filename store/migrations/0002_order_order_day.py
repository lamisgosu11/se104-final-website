from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('store','0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_day',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]