# Generated by Django 2.1.8 on 2019-06-29 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subsmanager', '0002_auto_20190629_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom',
            name='lastpay',
        ),
    ]