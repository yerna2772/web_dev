from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30, default='company')
    description = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=30, default='')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, default='')
    salary = models.FloatField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
        }


# Create your models here.
