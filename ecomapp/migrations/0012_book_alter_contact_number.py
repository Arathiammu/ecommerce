# Generated by Django 4.2.7 on 2023-12-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0011_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=17)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(max_length=10),
        ),
    ]
