# Generated by Django 3.1.7 on 2021-04-11 11:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20210406_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='room_no',
            new_name='class_name',
        ),
        migrations.AddField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(default=0, unique=True, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='class',
            name='room_no',
            field=models.IntegerField(default=0, unique=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)]),
        ),
    ]
