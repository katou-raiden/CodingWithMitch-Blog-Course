# Generated by Django 2.2.2 on 2019-06-17 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_auto_20190617_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='person_name',
            new_name='title',
        ),
    ]
