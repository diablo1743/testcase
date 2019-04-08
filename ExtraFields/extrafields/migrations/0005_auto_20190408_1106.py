# Generated by Django 2.2 on 2019-04-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extrafields', '0004_auto_20190408_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='title',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='eyecolor',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='eyecolor',
            name='title',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]