# Generated by Django 2.2.12 on 2022-04-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webProject', '0002_auto_20220405_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
