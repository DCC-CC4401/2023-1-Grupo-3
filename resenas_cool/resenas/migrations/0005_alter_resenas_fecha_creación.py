# Generated by Django 4.2 on 2023-05-13 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resenas', '0004_remove_resenas_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resenas',
            name='fecha_creación',
            field=models.DateField(default='2023-05-13'),
        ),
    ]
