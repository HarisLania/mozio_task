# Generated by Django 4.0.4 on 2022-06-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=64, unique=True)),
                ('email', models.EmailField(max_length=256, unique=True)),
                ('language', models.CharField(max_length=64)),
                ('currency', models.CharField(max_length=64)),
            ],
        ),
    ]
