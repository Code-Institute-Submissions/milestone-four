# Generated by Django 3.0.5 on 2020-05-29 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_auto_20200521_1841'),
        ('shop', '0010_auto_20200521_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='order',
        ),
        migrations.AddField(
            model_name='reviews',
            name='work_item',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='works.work_items'),
        ),
        migrations.AddField(
            model_name='shop_items',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shop_items',
            name='personal_message',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
