# Generated by Django 3.1.7 on 2021-08-05 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_transfer_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer_history',
            name='receiver',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transfer_history',
            name='sender',
            field=models.CharField(max_length=255),
        ),
    ]
