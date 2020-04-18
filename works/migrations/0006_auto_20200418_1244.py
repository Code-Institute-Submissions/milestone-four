# Generated by Django 3.0.5 on 2020-04-18 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0005_auto_20200418_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='work_sizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='work_items',
            name='work_size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='works.work_sizes'),
        ),
    ]
