# Generated by Django 4.1.6 on 2023-04-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book1", "0002_alter_booking_time_slot"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="date",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
