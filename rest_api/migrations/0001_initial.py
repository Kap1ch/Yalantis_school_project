# Generated by Django 3.2.9 on 2021-12-12 16:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='first name')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date create')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Date update')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50, verbose_name='make')),
                ('model', models.CharField(max_length=50, verbose_name='model')),
                ('plate_number', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex='^[A-Z]{2} \\d{4} [A-Z]{2}$')], verbose_name='plate_number')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Date create')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Date update')),
                ('driver_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest_api.driver')),
            ],
        ),
    ]