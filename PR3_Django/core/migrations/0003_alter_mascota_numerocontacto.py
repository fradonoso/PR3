# Generated by Django 3.2.4 on 2021-07-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_mascota_numerocontacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='numeroContacto',
            field=models.CharField(max_length=11, verbose_name='Numero de contacto'),
        ),
    ]
