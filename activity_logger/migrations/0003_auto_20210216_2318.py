# Generated by Django 3.0.3 on 2021-02-16 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_logger', '0002_auto_20210216_2312'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Activity',
            new_name='ActivityData',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='UserData',
        ),
    ]
