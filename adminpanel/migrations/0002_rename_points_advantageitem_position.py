# Generated by Django 5.0 on 2023-12-28 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advantageitem',
            old_name='points',
            new_name='position',
        ),
    ]
