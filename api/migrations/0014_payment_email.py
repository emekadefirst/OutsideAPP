# Generated by Django 5.0.2 on 2024-02-26 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_payment_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
