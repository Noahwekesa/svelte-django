# Generated by Django 5.0.1 on 2024-01-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('director', models.CharField(max_length=98)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
