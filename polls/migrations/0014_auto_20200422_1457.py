# Generated by Django 3.0.3 on 2020-04-22 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20200422_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='c_traitmentdate',
        ),
        migrations.AddField(
            model_name='check',
            name='c_traitment',
            field=models.BooleanField(default=False),
        ),
    ]