# Generated by Django 3.1.2 on 2022-04-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220411_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente_fonoaudiologia',
            name='feedback',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paciente_fonoaudiologia',
            name='audio_wav',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='paciente_fonoaudiologia',
            name='video',
            field=models.FileField(upload_to=''),
        ),
    ]
