# Generated by Django 5.2 on 2025-04-22 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_category_employee_menu_order_orderitem_delete_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='is_delivered',
            field=models.BooleanField(default=False),
        ),
    ]
