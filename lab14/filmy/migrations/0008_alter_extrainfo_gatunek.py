# Generated by Django 5.0.6 on 2024-06-03 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0007_alter_extrainfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(3, 'Sci-fi'), (2, 'Komedia'), (1, 'Horror'), (0, 'Inne'), (4, 'Dramat')], null=True),
        ),
    ]
