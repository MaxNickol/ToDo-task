# Generated by Django 3.1.2 on 2020-11-01 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_auto_20201031_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do',
            name='time_creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]