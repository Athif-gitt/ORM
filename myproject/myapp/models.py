from django.db import models

class Student(models.Model):
    name = models.CharField(max_length= 100)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
class Course(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    enrolled_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.student} => {self.course}"

