# Generated by Django 4.0.5 on 2022-07-11 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Digital_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='registered_user',
            table='RegisteredUser',
        ),
        migrations.AlterModelTable(
            name='user_data',
            table='UserData',
        ),
    ]
