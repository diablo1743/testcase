# Generated by Django 2.2 on 2019-04-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extrafields', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='description',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='eyecolor',
            name='description',
            field=models.TextField(max_length=100, null=True),
        ),
    ]