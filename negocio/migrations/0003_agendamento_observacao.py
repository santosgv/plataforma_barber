# Generated by Django 4.0.3 on 2022-06-29 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0002_alter_agendamento_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='observacao',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
