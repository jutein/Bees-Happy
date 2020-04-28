# Generated by Django 3.0.3 on 2020-02-23 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_check_hive_metric_hive'),
    ]

    operations = [
        migrations.AddField(
            model_name='check_hive',
            name='Restiction',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='check_hive',
            name='add_queen_cell',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='check_hive',
            name='id_hive',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='check_hive',
            name='queen_cells',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='metric_hive',
            name='id_hive',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='metric_hive',
            name='temperature',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='metric_hive',
            name='weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='check_hive',
            name='nb_cadrecouvain',
            field=models.IntegerField(default=0),
        ),
    ]
