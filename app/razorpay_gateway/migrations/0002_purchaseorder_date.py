# Generated by Django 2.1.7 on 2019-07-05 07:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('razorpay_gateway', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
