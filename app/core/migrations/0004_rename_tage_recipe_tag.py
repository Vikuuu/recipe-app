# Generated by Django 3.2.25 on 2024-08-06 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20240806_0718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='tage',
            new_name='tag',
        ),
    ]
