# Generated by Django 5.0.2 on 2024-02-24 14:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_host_phone_number'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.FloatField(default='0.00')),
                ('status', models.CharField(choices=[('SUCCESSFUL', 'Successful'), ('PENDING', 'Pending'), ('FAILED', 'Failed')], default='PENDING', max_length=50)),
                ('ref', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
