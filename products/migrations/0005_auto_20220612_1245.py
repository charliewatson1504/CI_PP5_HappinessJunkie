# Generated by Django 3.2.13 on 2022-06-12 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_friendly_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_foil_print_card_color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='has_foil_print_finish',
        ),
        migrations.RemoveField(
            model_name='product',
            name='has_sticker_finish',
        ),
    ]