# Generated by Django 4.0.5 on 2022-07-25 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Digital_app', '0002_alter_registered_user_table_alter_user_data_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='profile_image',
            field=models.FileField(default='image/user.png', upload_to='images/'),
        ),
    ]