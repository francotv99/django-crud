# Generated by Django 5.0 on 2023-12-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='pais',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
