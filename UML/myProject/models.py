from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

class Professor(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class CourseSection(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    students = models.IntegerField(default=0)
    semester = models.CharField(max_length=10)
    academic_year = models.CharField(max_length=10)

class Research(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    funding = models.DecimalField(max_digits=15, decimal_places=2)
    papers_published = models.IntegerField(default=0)
