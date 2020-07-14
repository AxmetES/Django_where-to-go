# Generated by Django 3.0.7 on 2020-07-14 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_image_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image']},
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default=0, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.Place'),
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
