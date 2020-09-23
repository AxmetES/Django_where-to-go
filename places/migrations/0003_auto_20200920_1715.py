# Generated by Django 3.0.7 on 2020-09-20 11:15

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20200905_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='placeId',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.CharField(blank=True, max_length=200, verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
