# Generated by Django 3.0.7 on 2020-07-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0006_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='two_explaination',
            name='percent',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
