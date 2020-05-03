# Generated by Django 3.0.5 on 2020-05-03 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200503_2055'),
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_items',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='works.categories'),
        ),
        migrations.AlterField(
            model_name='work_items',
            name='shop_settings',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shop_items'),
        ),
    ]
