# Generated by Django 4.1.6 on 2023-04-27 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Credentials",
            fields=[
                (
                    "Email",
                    models.CharField(max_length=60, primary_key=True, serialize=False),
                ),
                ("Password", models.CharField(max_length=30)),
            ],
            options={
                "db_table": "User",
            },
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=30)),
                ("Sn_Sc", models.CharField(max_length=30)),
                ("date", models.DateTimeField(blank=True, null=True)),
                ("room", models.CharField(max_length=20)),
                ("time_slot", models.DateTimeField(blank=True, null=True)),
                ("reason", models.CharField(max_length=200)),
                (
                    "Email",
                    models.ForeignKey(
                        blank=True,
                        db_column="Email",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="email",
                        to="book1.credentials",
                    ),
                ),
            ],
            options={
                "db_table": "Book1",
            },
        ),
    ]
