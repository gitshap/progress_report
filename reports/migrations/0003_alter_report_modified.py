# Generated by Django 3.2.9 on 2022-01-07 03:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20220107_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='modified',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
