# Generated by Django 3.0.3 on 2021-02-17 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity_logger', '0003_auto_20210216_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitydata',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='activity_logger.UserData'),
        ),
    ]
