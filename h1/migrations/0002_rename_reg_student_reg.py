# Generated by Django 4.0.1 on 2022-01-09 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('h1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Reg',
            new_name='reg',
        ),
    ]
