# Generated by Django 5.0.3 on 2024-04-05 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_streamer_anime_streamer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='Streamer',
            new_name='streamer',
        ),
        migrations.AlterField(
            model_name='phasing',
            name='date',
            field=models.DateField(verbose_name='Phasing Date'),
        ),
    ]
