# Generated by Django 4.0.4 on 2022-04-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mashina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
                ('rangi', models.CharField(max_length=26)),
                ('yili', models.DateTimeField()),
                ('yili1', models.DateField()),
                ('narxi', models.SmallIntegerField(max_length=25)),
                ('time_creat', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateField(auto_now=True)),
            ],
        ),
    ]
