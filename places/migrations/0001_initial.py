# Generated by Django 3.0.7 on 2020-07-06 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeId', models.TextField(null=True)),
                ('title', models.TextField()),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('file', models.FilePathField(path='/home/blasphemous/Desktop/my_projects/django/django-where-to-go/media')),
                ('place', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.Place')),
            ],
        ),
    ]