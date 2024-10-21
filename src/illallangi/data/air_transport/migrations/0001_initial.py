# Generated by Django 5.1.2 on 2024-10-21 04:25

import autoslug.fields
import django.db.models.deletion
import timezone_field.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aviation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='get_slug', unique_with=('start__year', 'start__month', 'start__day'))),
                ('start', models.DateField()),
                ('name', models.CharField(max_length=64)),
                ('end', models.DateField(max_length=25)),
            ],
            options={
                'unique_together': {('start', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='get_slug', unique_with=('departure__year', 'departure__month', 'departure__day'))),
                ('departure', models.DateTimeField()),
                ('flight_number', models.CharField(max_length=6)),
                ('arrival', models.DateTimeField(max_length=25)),
                ('arrival_timezone', timezone_field.fields.TimeZoneField()),
                ('departure_timezone', timezone_field.fields.TimeZoneField()),
                ('destination_city', models.CharField(max_length=255)),
                ('passenger', models.CharField(max_length=255)),
                ('destination_terminal', models.CharField(max_length=255)),
                ('destination_gate', models.CharField(max_length=255)),
                ('flight_class', models.CharField(max_length=255)),
                ('origin_city', models.CharField(max_length=255)),
                ('origin_gate', models.CharField(max_length=255)),
                ('origin_terminal', models.CharField(max_length=255)),
                ('sequence_number', models.CharField(max_length=3)),
                ('seat', models.CharField(max_length=3)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='aviation.airline')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_flights', to='aviation.airport')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='originating_flights', to='aviation.airport')),
            ],
            options={
                'unique_together': {('departure', 'slug')},
            },
        ),
    ]
