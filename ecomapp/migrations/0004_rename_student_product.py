# Generated by Django 4.2.7 on 2023-12-12 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0003_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Product',
        ),
    ]