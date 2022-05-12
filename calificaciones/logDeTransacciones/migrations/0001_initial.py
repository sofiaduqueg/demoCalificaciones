# Generated by Django 4.0.3 on 2022-04-04 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('parqueadero', models.BooleanField()),
                ('pagoPorSemestre', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDeVivienda', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('vivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulacionVivienda.vivienda')),
            ],
        ),
    ]
