# Generated by Django 4.2 on 2023-06-05 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resenas', '0012_remove_resenas_valoracion_valoracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='resenas',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='resenas',
            name='fecha_creación',
            field=models.DateField(default='2023-06-05'),
        ),
    ]
