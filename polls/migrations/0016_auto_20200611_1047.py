# Generated by Django 3.0.3 on 2020-06-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20200611_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiaries',
            name='a_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='u_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]