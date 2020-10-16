from django.db import models


# Create your models here.
class Company(models.Model):
    org_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.org_name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    ctc = models.IntegerField()
    company = models.ForeignKey(Company, related_name='employee_details', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
