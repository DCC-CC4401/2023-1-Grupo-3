# Generated by Django 4.2 on 2023-05-12 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resenas', '0003_alter_resenas_fecha_creación'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resenas',
            name='foto',
        ),
    ]