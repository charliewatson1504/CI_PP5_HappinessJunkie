# Generated by Django 3.2.13 on 2022-06-13 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_rename_original_bag_order_original_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivery_cost',
            new_name='shipping_cost',
        ),
    ]
