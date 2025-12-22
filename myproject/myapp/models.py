from django.db import models

# class Student(models.Model):
#     name = models.CharField(max_length= 100)
#     department = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
    
    
# class Course(models.Model):
#     title = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title
    
    
# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
#     enrolled_at = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return f"{self.student} => {self.course}"

# from django.db.models import Q
# # Bridgeon.objects.('id')
# Bridgeon.objects.filter(Q('id'))

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Menu(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name="menus"
    )
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name
    
    # Get all available menu items with hotel name
        
    # Filter menu items by hotel city Kozhikode

# Hotel.objects.bulk_create(('name', 'ABC'),('City', 'Calicut'))

# Menu.objects.select_related()

# items = Menu.objects.select_related('hotel').filter(city='Kozhikode')
# for item in items:
#     print(item.hotel.city, item.item_name)


