# Generated by Django 4.2.11 on 2025-01-07 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0024_alter_filmwork_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='creation_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата создания'),
        ),
    ]