# Generated by Django 3.0.3 on 2020-04-17 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_metric_hive_hive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apiaries',
            fields=[
                ('a_name', models.CharField(max_length=15)),
                ('a_id', models.IntegerField(primary_key=True, serialize=False)),
                ('a_idgateway', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_datetime', models.DateTimeField(auto_now_add=True)),
                ('c_globalstatus', models.CharField(choices=[('E', 'EXCELLENT'), ('B', 'BON'), ('M', 'MOYEN'), ('A', 'MAUVAIS')], max_length=10)),
                ('c_swarmsigns', models.BooleanField(default=False)),
                ('c_foodframenb', models.IntegerField(default=0)),
                ('c_foodquality', models.CharField(choices=[('M', 'MAXIMUM'), ('S', 'SUFFISANTE'), ('O', 'MOYENNE'), ('C', 'A COMPLETER'), ('V', 'VIDE')], max_length=15)),
                ('c_broodframenb', models.IntegerField(default=3)),
                ('c_broodframequality', models.CharField(choices=[('F', 'TRES REMPLI'), ('C', 'COMPLET'), ('N', 'NORMAL'), ('P', 'PARTIEL'), ('V', 'VIDE')], max_length=15)),
                ('c_queencellsnb', models.IntegerField(default=0)),
                ('c_queencellsextract', models.IntegerField(default=0)),
                ('c_queencelladded', models.IntegerField(default=0)),
                ('c_queencellsdestroid', models.IntegerField(default=0)),
                ('c_aggressive', models.BooleanField(default=False)),
                ('c_dronebrood', models.CharField(choices=[('E', 'EXCES'), ('N', 'NORMAL'), ('A', 'FAIBLE')], max_length=10)),
                ('c_drone', models.CharField(choices=[('E', 'EXCES'), ('N', 'NORMAL'), ('A', 'FAIBLE')], max_length=10)),
                ('c_traitmentdate', models.DateTimeField()),
                ('c_tratmenttype', models.CharField(choices=[('A', 'APIVAR'), ('X', 'XXX'), ('Y', 'YYY')], max_length=15)),
                ('c_sicknesssigns', models.BooleanField(default=False)),
                ('c_sickness', models.CharField(max_length=15)),
                ('c_super1', models.BooleanField(default=False)),
                ('c_superstate1', models.CharField(choices=[('P', 'PLEIN'), ('M', 'MOYEN'), ('V', 'VIDE')], max_length=15)),
                ('c_super2', models.BooleanField(default=False)),
                ('c_superstate2', models.CharField(choices=[('P', 'PLEIN'), ('M', 'MOYEN'), ('V', 'VIDE')], max_length=15)),
                ('c_super3', models.BooleanField(default=False)),
                ('c_superstate3', models.CharField(choices=[('P', 'PLEIN'), ('M', 'MOYEN'), ('V', 'VIDE')], max_length=15)),
                ('c_super4', models.BooleanField(default=False)),
                ('c_superstate4', models.CharField(choices=[('P', 'PLEIN'), ('M', 'MOYEN'), ('V', 'VIDE')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Hive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid_id', models.IntegerField(default=99)),
                ('h_swarmdate', models.DateTimeField()),
                ('h_queendate', models.DateTimeField()),
                ('h_queentype', models.CharField(choices=[('CA', 'CAUCASE'), ('NO', 'NOIRE'), ('IN', 'INCONNUE'), ('XX', 'XXXX')], max_length=10)),
                ('h_queencolor', models.CharField(choices=[('B', 'BLUE'), ('W', 'WHITE'), ('Y', 'YELLOW'), ('R', 'RED'), ('G', 'GREEN')], max_length=6)),
                ('h_model', models.CharField(choices=[('D', 'DADANT'), ('L', 'LANGSTROTH'), ('W', 'WARRE'), ('K', 'KENYANE'), ('V', 'VOIRNOT'), ('P', 'PAILLE'), ('A', 'AUTRE')], max_length=10)),
                ('h_framenb', models.BigIntegerField(default=10)),
                ('h_fkapiary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Apiaries')),
            ],
        ),
        migrations.RenameField(
            model_name='check_hive',
            old_name='id_hive',
            new_name='rfid_hive',
        ),
        migrations.RenameField(
            model_name='metric_env',
            old_name='acq_date',
            new_name='me_date',
        ),
        migrations.RenameField(
            model_name='metric_env',
            old_name='humidite',
            new_name='me_measure',
        ),
        migrations.RenameField(
            model_name='metric_hive',
            old_name='acq_date',
            new_name='mh_date',
        ),
        migrations.RenameField(
            model_name='metric_hive',
            old_name='sound',
            new_name='mh_measure',
        ),
        migrations.RemoveField(
            model_name='metric_env',
            name='id_rucher',
        ),
        migrations.RemoveField(
            model_name='metric_env',
            name='luminosite',
        ),
        migrations.RemoveField(
            model_name='metric_env',
            name='pluie',
        ),
        migrations.RemoveField(
            model_name='metric_env',
            name='pression',
        ),
        migrations.RemoveField(
            model_name='metric_env',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='metric_hive',
            name='hive',
        ),
        migrations.RemoveField(
            model_name='metric_hive',
            name='humidite',
        ),
        migrations.RemoveField(
            model_name='metric_hive',
            name='id_hive',
        ),
        migrations.RemoveField(
            model_name='metric_hive',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='metric_hive',
            name='weight',
        ),
        migrations.AddField(
            model_name='metric_env',
            name='me_type',
            field=models.CharField(default=1, max_length=1),
        ),
        migrations.AddField(
            model_name='metric_hive',
            name='mh_type',
            field=models.CharField(choices=[('T', 'TEMP'), ('P', 'PRES'), ('H', 'HUMI'), ('S', 'SOUN')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='check',
            name='c_fkhive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Hive'),
        ),
        migrations.AddField(
            model_name='metric_env',
            name='me_fkapiariy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Apiaries'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metric_hive',
            name='mh_fkhive',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Hive'),
            preserve_default=False,
        ),
    ]