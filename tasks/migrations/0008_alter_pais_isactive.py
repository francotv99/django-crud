# Generated by Django 5.0 on 2023-12-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_pais_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]