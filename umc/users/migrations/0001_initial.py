# Generated by Django 4.1.3 on 2022-11-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("date_of_birth", models.DateField()),
                ("IIN", models.IntegerField()),
                ("id_patient", models.IntegerField()),
                ("name", models.CharField(max_length=255)),
                ("blood_group", models.CharField(max_length=255)),
                ("contact_num", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=255)),
                ("martial_status", models.CharField(max_length=255)),
                ("reg_date", models.DateField()),
                ("other", models.TextField()),
            ],
        ),
    ]
