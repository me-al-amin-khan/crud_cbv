from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class School(models.Model):
    school_type = [
        ('boys_school', 'Boys School'),
        ('girls_school', 'Girls School'),
        ('coeducation_school', 'Codecuation School'),
    ]

    school_name = models.CharField(max_length=120)
    school_type = models.CharField(max_length=20, choices=school_type, default='coeducation_school')
    principal_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse_lazy('detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.school_name



class Student(models.Model):
    student_name = models.CharField(max_length=150)
    roll_number = models.PositiveIntegerField(null=True)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, related_name = 'student')

    def __str__(self):
        return self.student_name
