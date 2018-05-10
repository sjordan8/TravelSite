# Generated by Django 2.0.2 on 2018-05-09 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180424_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip_model',
            name='image',
            field=models.ImageField(default='NO IMAGE', max_length=150, upload_to='uploads/%Y/%M/%D'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip_model',
            name='image_description',
            field=models.CharField(default='NO IMAGE', max_length=40),
            preserve_default=False,
        ),
    ]