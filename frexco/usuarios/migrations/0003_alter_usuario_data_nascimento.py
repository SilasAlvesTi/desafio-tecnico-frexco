# Generated by Django 4.1.2 on 2022-10-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_senha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='data_nascimento',
            field=models.DateField(max_length=8),
        ),
    ]
