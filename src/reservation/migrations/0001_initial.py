# Generated by Django 2.1.5 on 2021-06-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('room_type', models.CharField(choices=[('double', 'DOUBLE'), ('twin', 'TWIN'), ('ben in a hostel', 'BED IN A HOSTEL'), ('studio', 'STUDIO')], default='double', max_length=15)),
                ('notes', models.TextField()),
            ],
        ),
    ]
