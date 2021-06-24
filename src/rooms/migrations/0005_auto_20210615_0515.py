# Generated by Django 2.1.5 on 2021-06-15 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20210614_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='bed_type',
            field=models.CharField(blank=True, choices=[('Queen', 'queen'), ('Single', 'single'), ('Twin', 'twin')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='size',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
    ]
