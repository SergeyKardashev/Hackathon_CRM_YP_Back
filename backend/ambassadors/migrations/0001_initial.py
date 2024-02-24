# Generated by Django 4.2.10 on 2024-02-23 16:05

import ambassadors.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambassadors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(verbose_name='дата регистрации')),
                ('surname', models.CharField(max_length=250, verbose_name='фамилия')),
                ('name', models.CharField(max_length=250, verbose_name='имя')),
                ('patronymic', models.CharField(max_length=250, null=True, verbose_name='отчество')),
                ('gender', models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], max_length=1)),
                ('country', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('zip_code', models.CharField(max_length=6, validators=[ambassadors.validators.validate_index])),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('phone', models.CharField(max_length=11, unique=True, validators=[ambassadors.validators.validate_phone])),
                ('telegram_handle', models.CharField(max_length=250, validators=[ambassadors.validators.validate_tg_handle])),
                ('education', models.CharField(max_length=250)),
                ('job', models.CharField(max_length=250)),
                ('aim', models.TextField()),
                ('want_to_do', models.CharField(max_length=250)),
                ('blog_url', models.URLField(null=True, unique=True)),
                ('shirt_size', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=2)),
                ('shoes_size', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(70)])),
                ('comment', models.TextField(null=True)),
                ('promocode', models.CharField(max_length=250, null=True)),
                ('status', models.CharField(choices=[('active', 'Активный'), ('inactive', 'Не активный')], max_length=8, null=True)),
            ],
            options={
                'ordering': ('surname', 'name', 'patronymic', 'date_created'),
            },
        ),
    ]
