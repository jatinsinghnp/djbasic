# Generated by Django 3.2.3 on 2021-06-05 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogmodel_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]