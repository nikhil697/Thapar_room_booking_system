# Generated by Django 4.1.6 on 2023-04-27 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book1", "0003_alter_booking_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
