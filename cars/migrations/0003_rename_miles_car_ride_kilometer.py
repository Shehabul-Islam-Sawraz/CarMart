# Generated by Django 3.2.9 on 2021-12-22 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20211222_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='miles',
            new_name='ride_kilometer',
        ),
    ]