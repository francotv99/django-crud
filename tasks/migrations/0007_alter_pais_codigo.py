# Generated by Django 5.0 on 2023-12-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_estado_codigo_alter_pais_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='codigo',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
