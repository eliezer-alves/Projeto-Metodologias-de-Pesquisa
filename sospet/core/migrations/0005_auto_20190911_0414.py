# Generated by Django 2.2.2 on 2019-09-11 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190911_0408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='bedrooms',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='peoples',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='price',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='toilets',
        ),
    ]
