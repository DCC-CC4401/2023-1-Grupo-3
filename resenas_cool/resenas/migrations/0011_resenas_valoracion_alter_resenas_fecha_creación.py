# Generated by Django 4.2 on 2023-06-01 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resenas', '0010_alter_categorias_nombre_alter_resenas_fecha_creación'),
    ]

    operations = [
        migrations.AddField(
            model_name='resenas',
            name='valoracion',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='resenas',
            name='fecha_creación',
            field=models.DateField(default='2023-06-01'),
        ),
    ]
