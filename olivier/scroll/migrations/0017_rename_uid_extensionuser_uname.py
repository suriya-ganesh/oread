# Generated by Django 4.0 on 2022-01-19 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scroll', '0016_extensionuser_uid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extensionuser',
            old_name='uid',
            new_name='uname',
        ),
    ]
