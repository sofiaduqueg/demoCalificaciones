# Generated by Django 4.0.3 on 2022-03-16 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calificacionesPsicologos', '0003_psicologo_promedio_calificaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='psicologo',
            name='cantidad_calificaciones',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
