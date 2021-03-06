# Generated by Django 3.0.3 on 2020-04-22 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20200422_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='c_broodframenb',
            field=models.IntegerField(blank=True, default=3),
        ),
        migrations.AlterField(
            model_name='check',
            name='c_broodframequality',
            field=models.CharField(blank=True, choices=[('F', 'TRES REMPLI'), ('C', 'COMPLET'), ('N', 'NORMAL'), ('P', 'PARTIEL'), ('V', 'VIDE')], max_length=15),
        ),
        migrations.AlterField(
            model_name='check',
            name='c_datetime',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='c_drone',
            field=models.CharField(blank=True, choices=[('E', 'EXCES'), ('N', 'NORMAL'), ('A', 'FAIBLE')], max_length=10),
        ),
        migrations.AlterField(
            model_name='check',
            name='c_dronebrood',
            field=models.CharField(blank=True, choices=[('E', 'EXCES'), ('N', 'NORMAL'), ('A', 'FAIBLE')], max_length=10),
        ),
        migrations.AlterField(
            model_name='check',
            name='c_foodframenb',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='check',
            name='c_foodquality',
            field=models.CharField(blank=True, choices=[('M', 'MAXIMUM'), ('S', 'SUFFISANTE'), ('O', 'MOYENNE'), ('C', 'A COMPLETER'), ('V', 'VIDE')], max_length=15),
        ),
        migrations.AlterField(
            model_name='check',
            name='c_sickness',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='check',
            name='c_superstate1',
            field=models.CharField(blank=True, choices=[('P', 'PLEIN'), ('M', 'MOYEN'), ('V', 'VIDE')], max_length=15),
        ),
        migrations.AlterField(
            model_name='check',
            name='c_superstate2',
            field=models.CharField(blank=True, choices=[('P', 'PLEIN'), ('M', 'MOYEN'), ('V', 'VIDE')], max_length=15),
        ),
        migrations.AlterField(
            model_name='check',
            name='c_superstate3',
            field=models.CharField(blank=True, choices=[('P', 'PLEIN'), ('M', 'MOYEN'), ('V', 'VIDE')], max_length=15),
        ),
        migrations.AlterField(
            model_name='check',
            name='c_superstate4',
            field=models.CharField(blank=True, choices=[('P', 'PLEIN'), ('M', 'MOYEN'), ('V', 'VIDE')], max_length=15),
        ),
        migrations.AlterField(
            model_name='check',
            name='c_traitmentdate',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='c_tratmenttype',
            field=models.CharField(blank=True, choices=[('A', 'APIVAR'), ('X', 'XXX'), ('Y', 'YYY')], max_length=15),
        ),
    ]
