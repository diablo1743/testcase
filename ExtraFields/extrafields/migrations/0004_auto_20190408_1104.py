# Generated by Django 2.2 on 2019-04-08 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extrafields', '0003_auto_20190406_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='title',
            field=models.CharField(db_index=True, default='Russia', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='eyecolor',
            name='title',
            field=models.CharField(db_index=True, default='Russia', max_length=100, unique=True),
        ),
    ]