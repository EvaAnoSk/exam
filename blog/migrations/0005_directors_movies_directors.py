# Generated by Django 5.1.1 on 2024-09-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_actors_date_of_birth_movies_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('text', models.TextField()),
                ('date_of_birth', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='movies',
            name='directors',
            field=models.ManyToManyField(to='blog.directors'),
        ),
    ]
