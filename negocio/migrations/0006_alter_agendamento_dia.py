# Generated by Django 4.0.5 on 2022-06-29 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0005_alter_agendamento_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='dia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='negocio.dia'),
        ),
    ]