# Generated by Django 4.0.4 on 2022-04-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mashina',
            name='narxi',
            field=models.SmallIntegerField(),
        ),
    ]
