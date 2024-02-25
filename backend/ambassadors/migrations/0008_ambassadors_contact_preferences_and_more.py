# Generated by Django 4.2.10 on 2024-02-24 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambassadors', '0007_alter_ambassadors_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambassadors',
            name='contact_preferences',
            field=models.CharField(choices=[('email', 'email'), ('phone', 'phone'), ('telegram', 'telegram')], max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='ambassadors',
            name='supervisor_comment',
            field=models.TextField(null=True),
        ),
    ]
