# Generated by Django 5.0.2 on 2024-02-14 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_host_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='phone_number',
            field=models.CharField(default='None', max_length=14),
        ),
    ]
