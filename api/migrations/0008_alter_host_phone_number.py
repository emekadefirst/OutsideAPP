# Generated by Django 5.0.2 on 2024-02-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_host_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]
