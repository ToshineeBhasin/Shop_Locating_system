# Generated by Django 3.1.7 on 2021-04-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoplocatingapp', '0011_auto_20210315_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='shopid',
            field=models.IntegerField(default=0),
        ),
    ]
