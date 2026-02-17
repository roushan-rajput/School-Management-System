from django.db import models
# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    City = models.CharField()
    Age = models.CharField()
    Contact=models.CharField()
    Image=models.ImageField()
    Password=models.CharField()
    Cpassword=models.CharField()

    def __str__(self):
        return self.Name