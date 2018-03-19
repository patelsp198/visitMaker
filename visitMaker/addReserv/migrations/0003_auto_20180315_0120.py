# Generated by Django 2.0.2 on 2018-03-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addReserv', '0002_auto_20180314_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='tour_time',
            field=models.IntegerField(choices=[('10am', '10:00am-11:00pm'), ('11am', '11:00am-12:00pm'), ('12pm', '12:00pm-1:00pm'), ('1pm', '1:00pm-2:00pm')], max_length=20),
        ),
    ]
