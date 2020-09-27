# Generated by Django 3.0.8 on 2020-09-27 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=120, verbose_name='First Name')),
                ('mname', models.CharField(max_length=120, verbose_name='Middle Name')),
                ('lname', models.CharField(max_length=120, verbose_name='Last Name')),
                ('donation_date', models.DateTimeField(default=datetime.datetime(2020, 9, 27, 10, 30, 22, 557651), verbose_name='Date of Donation')),
                ('quantity', models.IntegerField(null=True, verbose_name='Quantity')),
                ('itamname', models.CharField(max_length=120, verbose_name='Item')),
            ],
        ),
    ]
