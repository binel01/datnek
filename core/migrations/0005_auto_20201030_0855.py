# Generated by Django 2.2 on 2020-10-30 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201030_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagelevel',
            name='language',
            field=models.IntegerField(choices=[(1, 'Français'), (2, 'Anglais'), (3, 'Néerlandais'), (4, 'Courrant')], verbose_name='Langue'),
        ),
    ]