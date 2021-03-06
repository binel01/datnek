# Generated by Django 2.2 on 2020-10-29 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagelevel',
            name='speaking_level',
            field=models.IntegerField(choices=[(1, 'Elementary'), (2, 'Pre-intermediate'), (3, 'Intermediate'), (4, 'Current')], verbose_name='Speaking'),
        ),
        migrations.AlterField(
            model_name='languagelevel',
            name='understanding_level',
            field=models.IntegerField(choices=[(1, 'Elementary'), (2, 'Pre-intermediate'), (3, 'Intermediate'), (4, 'Current')], verbose_name='Understanding'),
        ),
        migrations.AlterField(
            model_name='languagelevel',
            name='writting_level',
            field=models.IntegerField(choices=[(1, 'Elementary'), (2, 'Pre-intermediate'), (3, 'Intermediate'), (4, 'Current')], verbose_name='Writting'),
        ),
    ]
