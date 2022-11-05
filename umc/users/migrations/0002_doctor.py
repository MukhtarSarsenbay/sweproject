# Generated by Django 4.1.3 on 2022-11-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor",
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
                ("id_doctor", models.IntegerField()),
                ("name", models.CharField(max_length=255)),
                ("contact_num", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("department_id", models.IntegerField()),
                ("spec_id", models.IntegerField()),
                ("experience_in_years", models.IntegerField()),
                ("photo", models.ImageField(upload_to="")),
                ("category", models.CharField(max_length=120)),
                ("appoinment_price", models.FloatField()),
                ("schedule", models.TextField()),
                ("degree", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=255)),
                ("homepage_url", models.CharField(max_length=255)),
            ],
        ),
    ]