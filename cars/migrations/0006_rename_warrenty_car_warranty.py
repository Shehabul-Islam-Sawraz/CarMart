# Generated by Django 3.2.9 on 2021-12-23 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_warrenty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='warrenty',
            new_name='warranty',
        ),
    ]
