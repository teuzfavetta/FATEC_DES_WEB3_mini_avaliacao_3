# Generated by Django 4.2 on 2023-04-13 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feriadomodel',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado em: '),
        ),
        migrations.AlterField(
            model_name='feriadomodel',
            name='nome',
            field=models.CharField(max_length=60, verbose_name='Feriado'),
        ),
    ]
