from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    enrollment_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
