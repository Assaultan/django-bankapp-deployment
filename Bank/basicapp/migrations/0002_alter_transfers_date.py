# Generated by Django 3.2.3 on 2021-08-03 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfers',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
