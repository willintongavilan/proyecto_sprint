# Generated by Django 4.1.1 on 2022-09-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
            ],
        ),
    ]
