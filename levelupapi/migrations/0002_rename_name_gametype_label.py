# Generated by Django 3.2.9 on 2021-12-15 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gametype',
            old_name='name',
            new_name='label',
        ),
    ]
