# Generated by Django 3.2 on 2022-03-28 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220327_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='categoria',
            field=models.IntegerField(choices=[[0, 'Alimentacion'], [1, 'Medicamentos'], [2, 'Agenda Medica'], [3, 'Fonoaudiologia']], default=1),
            preserve_default=False,
        ),
    ]
