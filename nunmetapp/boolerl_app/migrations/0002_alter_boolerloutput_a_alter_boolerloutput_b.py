# Generated by Django 4.2.7 on 2023-11-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boolerl_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boolerloutput',
            name='a',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='boolerloutput',
            name='b',
            field=models.FloatField(default=1),
        ),
    ]
