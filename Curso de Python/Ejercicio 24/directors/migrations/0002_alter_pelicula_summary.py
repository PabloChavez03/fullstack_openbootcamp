# Generated by Django 4.1 on 2022-08-30 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='summary',
            field=models.TextField(help_text='Pon un resumen', max_length=400),
        ),
    ]
