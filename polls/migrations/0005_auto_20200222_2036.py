# Generated by Django 3.0.3 on 2020-02-23 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_metric_hive_acq_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_hive',
            name='chk_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
