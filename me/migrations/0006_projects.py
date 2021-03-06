# Generated by Django 3.0.7 on 2020-07-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0005_auto_20200701_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projimg')),
                ('feature', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=75)),
                ('link', models.URLField()),
                ('desc', models.TextField()),
            ],
        ),
    ]
