# Generated by Django 2.1.7 on 2019-07-25 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty', '0007_auto_20190724_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='date',
            field=models.CharField(default='Fri Jul 26 00:19:00 2019', max_length=50),
        ),
        migrations.AlterField(
            model_name='spendpoints',
            name='date',
            field=models.CharField(default='Fri Jul 26 00:19:00 2019', max_length=50),
        ),
    ]
