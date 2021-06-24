# Generated by Django 2.1.5 on 2021-06-14 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Категория номера',
                'verbose_name_plural': 'Категории номеров',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('size', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('bed_type', models.CharField(blank=True, choices=[('Q', 'queen'), ('S', 'single'), ('Tw', 'twin')], max_length=10, null=True)),
                ('room_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.RoomCategory')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='rooms',
            name='services',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rooms.Services'),
        ),
    ]