# Generated by Django 4.2 on 2023-04-04 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_women_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='women',
            old_name='users',
            new_name='user',
        ),
    ]
