# Generated by Django 5.1.4 on 2024-12-16 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_example_created_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Source',
            new_name='Collection',
        ),
        migrations.RenameField(
            model_name='context',
            old_name='pl',
            new_name='og',
        ),
        migrations.RenameField(
            model_name='context',
            old_name='en',
            new_name='tr',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='pl',
            new_name='og',
        ),
        migrations.RenameField(
            model_name='word',
            old_name='en',
            new_name='tr',
        ),
    ]
