# Generated by Django 4.0.3 on 2022-03-30 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliogestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]