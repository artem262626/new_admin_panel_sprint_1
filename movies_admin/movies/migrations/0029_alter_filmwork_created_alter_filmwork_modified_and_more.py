# Generated by Django 4.2.11 on 2025-01-11 11:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0028_alter_genre_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='genre',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='genre',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='person',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='person',
            name='modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]