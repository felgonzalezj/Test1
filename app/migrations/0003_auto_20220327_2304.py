# Generated by Django 3.2 on 2022-03-28 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220327_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='id',
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='id_publicacion',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
