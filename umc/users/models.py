from django.db import models

# Create your models here.


class Patient(models.Model):
    date_of_birth = models.DateField()
    IIN = models.IntegerField()
    id_patient = models.IntegerField()
    name = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=255)
    contact_num = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=255)
    martial_status = models.CharField(max_length=255)
    reg_date = models.DateField()
    other = models.TextField()


class Doctor(models.Model):
    date_of_birth = models.DateField()
    IIN = models.IntegerField()
    id_doctor = models.IntegerField()
    name = models.CharField(max_length=255)
    contact_num = models.IntegerField()
    email = models.EmailField()
    department_id = models.IntegerField()
    spec_id = models.IntegerField()
    experience_in_years = models.IntegerField()
    photo = models.ImageField()
    category = models.CharField(max_length=120)
    appoinment_price = models.FloatField()
    schedule = models.TextField()
    degree = models.CharField(max_length=100)
    rating = models.ValueRange(start=0, end=10)
    address = models.CharField(max_length=255)
    homepage_url = models.CharField(max_length=255)




