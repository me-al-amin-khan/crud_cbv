# Generated by Django 2.2.3 on 2019-07-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll_number',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]