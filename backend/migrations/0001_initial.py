# Generated by Django 3.1.2 on 2020-11-09 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField()),
                ('client_name', models.CharField(max_length=50)),
                ('client_type', models.CharField(max_length=30)),
            ],
        ),
    ]
