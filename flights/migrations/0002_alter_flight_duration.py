# Generated by Django 5.1.2 on 2024-10-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
