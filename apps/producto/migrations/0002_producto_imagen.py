# Generated by Django 3.2.3 on 2021-07-09 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='productos', verbose_name='Imagen del producto'),
        ),
    ]
