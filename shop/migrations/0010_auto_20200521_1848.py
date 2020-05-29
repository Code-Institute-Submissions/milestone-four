# Generated by Django 3.0.5 on 2020-05-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200521_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_items',
            name='coupon',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='shop_items',
            name='discount',
            field=models.SmallIntegerField(default=0),
        ),
    ]