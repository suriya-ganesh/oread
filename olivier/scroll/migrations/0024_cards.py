# Generated by Django 4.0 on 2022-05-07 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scroll', '0023_alter_extensionuser_uname_alter_extensionuser_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100, null=True)),
                ('visible', models.TextField(max_length=1000, null=True)),
                ('hidden', models.TextField(max_length=1000, null=True)),
            ],
        ),
    ]
