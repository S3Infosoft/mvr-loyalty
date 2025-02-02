# Generated by Django 2.1.7 on 2019-07-24 09:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('loyalty', '0002_auto_20190724_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='TryGuest',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('address', models.TextField(blank=True, null=True)),
                ('unique_id', models.CharField(default=uuid.uuid4, max_length=500, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
