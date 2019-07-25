# Generated by Django 2.1.7 on 2019-07-23 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cart_id', models.CharField(blank=True, default=uuid.uuid4, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('address', models.TextField(blank=True, null=True)),
                ('unique_id', models.CharField(default=uuid.uuid4, max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='default.png', null=None, upload_to='hotels_pics')),
                ('address', models.TextField()),
                ('contact_p_name', models.CharField(max_length=50)),
                ('contact_p_email', models.EmailField(blank=True, max_length=30)),
                ('contact_p_phone', models.CharField(max_length=12)),
                ('reward_ratio', models.FloatField(max_length=30)),
                ('unique_id', models.CharField(default=uuid.uuid4, max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_picss')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_t_hotel', models.DecimalField(decimal_places=2, max_digits=10)),
                ('points_obtain', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('unique_id', models.CharField(default=uuid.uuid4, max_length=500, unique=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loyalty.Guest')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='loyalty.Hotels')),
            ],
        ),
        migrations.CreateModel(
            name='RewardItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.FloatField(max_length=10)),
                ('item_description', models.TextField()),
                ('points_required', models.IntegerField()),
                ('item_image', models.ImageField(default='default_image.png', upload_to='reward_item_pics')),
                ('item_id', models.CharField(blank=True, default=uuid.uuid4, max_length=1000, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialDeals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_name', models.CharField(blank=True, default='no name', max_length=100)),
                ('description', models.TextField()),
                ('points_required', models.IntegerField()),
                ('original_price', models.FloatField(max_length=10)),
                ('deal_image', models.ImageField(default='deal.jpg', upload_to='deals_pics')),
                ('deal_id', models.CharField(blank=True, default=uuid.uuid4, max_length=1000)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='loyalty.Hotels')),
            ],
        ),
        migrations.CreateModel(
            name='SpendPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='loyalty.Guest')),
                ('reward_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='loyalty.RewardItem')),
                ('special_deals', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='loyalty.SpecialDeals')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='reward_items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='loyalty.RewardItem'),
        ),
        migrations.AddField(
            model_name='cart',
            name='special_deals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='loyalty.SpecialDeals'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
