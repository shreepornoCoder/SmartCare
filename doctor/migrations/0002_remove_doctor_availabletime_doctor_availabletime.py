# Generated by Django 5.0.6 on 2024-08-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='availableTime',
        ),
        migrations.AddField(
            model_name='doctor',
            name='availableTime',
            field=models.ManyToManyField(to='doctor.availabletime'),
        ),
    ]
