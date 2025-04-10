from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dept = models.CharField(max_length=100)
    mob = models.CharField(max_length=10)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
