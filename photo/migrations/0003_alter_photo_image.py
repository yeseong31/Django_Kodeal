# Generated by Django 4.0.3 on 2022-06-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
