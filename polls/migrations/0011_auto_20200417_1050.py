# Generated by Django 3.0.3 on 2020-04-17 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20200417_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settingg_app',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('as_appname', models.CharField(default='BEESHAPPY', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_id', models.IntegerField(primary_key=True, serialize=False)),
                ('u_firstname', models.CharField(max_length=20)),
                ('u_name', models.CharField(max_length=20)),
                ('u_mail', models.CharField(max_length=30, unique=True)),
                ('u_telephone', models.CharField(max_length=15)),
                ('u_etsname', models.CharField(max_length=20)),
                ('u_etsadresse', models.CharField(max_length=50)),
                ('u_etstown', models.CharField(max_length=30)),
                ('u_estcountry', models.CharField(max_length=20)),
                ('u_esttelephone', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='apiaries',
            name='a_fkuser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.User'),
            preserve_default=False,
        ),
    ]
