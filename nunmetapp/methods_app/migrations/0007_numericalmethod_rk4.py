# Generated by Django 4.2.7 on 2023-11-09 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rk4', '0001_initial'),
        ('methods_app', '0006_rename_booler_numericalmethod_boolerl'),
    ]

    operations = [
        migrations.AddField(
            model_name='numericalmethod',
            name='rk4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rk4.rk4'),
        ),
    ]