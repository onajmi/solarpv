# Generated by Django 3.1.2 on 2020-11-09 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_certificate_location_teststandard_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_id', models.IntegerField()),
                ('sequence_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.IntegerField()),
                ('service_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('fi_required', models.CharField(max_length=50)),
                ('fi_frequency', models.CharField(max_length=50)),
                ('standard_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.teststandard')),
            ],
        ),
    ]
