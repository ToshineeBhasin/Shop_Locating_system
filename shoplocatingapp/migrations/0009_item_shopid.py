# Generated by Django 3.1.7 on 2021-03-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoplocatingapp', '0008_auto_20210312_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='shopid',
            field=models.IntegerField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
