# Generated by Django 4.2.7 on 2023-12-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0008_remove_cart1_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart1',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
