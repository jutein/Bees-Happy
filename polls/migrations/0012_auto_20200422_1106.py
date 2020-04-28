# Generated by Django 3.0.3 on 2020-04-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20200417_1050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apiaries',
            options={'ordering': ['a_idgateway'], 'verbose_name': 'Mes rucher'},
        ),
        migrations.AlterModelOptions(
            name='check',
            options={'ordering': ['c_datetime'], 'verbose_name': 'Mes visites'},
        ),
        migrations.AlterModelOptions(
            name='hive',
            options={'ordering': ['rfid_id'], 'verbose_name': 'Mes ruches'},
        ),
        migrations.AlterModelOptions(
            name='metric_env',
            options={'ordering': ['me_date'], 'verbose_name': 'Mesures des ruchers'},
        ),
        migrations.AlterModelOptions(
            name='metric_hive',
            options={'ordering': ['mh_date'], 'verbose_name': 'Mesures ruches'},
        ),
        migrations.AlterField(
            model_name='metric_env',
            name='me_type',
            field=models.CharField(choices=[('T', 'TEMP'), ('P', 'PRES'), ('R', 'RAIN'), ('L', 'LIGH')], max_length=1),
        ),
    ]
