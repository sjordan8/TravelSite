# Generated by Django 2.0.2 on 2018-05-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20180510_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='num_people',
            field=models.IntegerField(default=0),
        ),
    ]
