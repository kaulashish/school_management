# Generated by Django 3.1.7 on 2021-04-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(choices=[(12, '12th'), (11, '11th'), (10, '10th'), (9, '9th'), (8, '8th')], max_length=100),
        ),
    ]
