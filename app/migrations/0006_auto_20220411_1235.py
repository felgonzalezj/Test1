# Generated by Django 3.1.2 on 2022-04-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente_Fonoaudiologia',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('audio_wav', models.FileField(upload_to='')),
                ('video', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterModelOptions(
            name='publicacion',
            options={'verbose_name': 'Publicacion', 'verbose_name_plural': 'Publicaciones'},
        ),
        migrations.AlterField(
            model_name='paciente',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
