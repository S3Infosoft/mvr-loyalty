# Generated by Django 2.1.7 on 2019-07-25 19:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('razorpay_gateway', '0003_auto_20190726_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='date',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
        ),
    ]
