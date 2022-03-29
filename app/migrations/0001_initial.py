# Generated by Django 3.2 on 2022-03-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_publicacion', models.IntegerField()),
                ('fecha_publicacion', models.DateField()),
                ('autor', models.IntegerField(choices=[[0, 'Admin'], [1, 'Staff']])),
                ('texto', models.TextField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
    ]