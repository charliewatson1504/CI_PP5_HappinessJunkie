# Generated by Django 3.2.13 on 2022-08-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_review_is_recommended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='is_recommended',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No'), (None, ' ')], default=None, null=True, verbose_name='Would you recommend this to a friend?'),
        ),
    ]