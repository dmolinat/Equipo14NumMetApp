# Generated by Django 4.2.7 on 2023-11-04 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('methods_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numericalmethod',
            name='inputs',
            field=models.JSONField(default={'test_input': 0}),
        ),
        migrations.AlterField(
            model_name='numericalmethod',
            name='outputs',
            field=models.JSONField(default={'test_output': 1}),
        ),
    ]
