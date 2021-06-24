from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class RoomCategory(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Категория номера'
        verbose_name_plural = 'Категории номеров'
    
    def __str__(self):
        return self.category_name
    
service_list = (
    ('Room Service 24/7', 'room service 24/7'),
    ('Airport Shuttle', 'airport shuttle'),
    ('Laundry Service 24/7', 'laundry service 24/7'),
    ('Free WiFi', 'free wifi')
)

class Services(models.Model):
    # service = models.MultiSelectField(choices=service_list, max_length=30, blank=True, null=True) 

    # class Meta:
    #     verbose_name = 'Услуга'
    #     verbose_name_plural = 'Услуги'
    
    # def __str__(self):
    #     return self.service
    pass
bed_type = (
    ('Queen', 'queen'),
    ('Single', 'single'),
    ('Twin', 'twin')
)

# class Homepage(models.Model):
#     description = models.TextField(blank=True)
#     image1 = models.ImageField(upload_to='rooms/', null=True)
#     image2 = models.ImageField(upload_to='rooms/', null=True)
#     image3 = models.ImageField(upload_to='rooms/', null=True)

#     class Meta:
#         verbose_name = 'Homepage Description'
#         verbose_name_plural = 'Homepage Descriptions'

    
class Rooms(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    room_category = models.ForeignKey('RoomCategory', on_delete=models.SET_NULL, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    size = models.DecimalField(decimal_places=0, max_digits=4, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    bed_type = models.CharField(choices=bed_type, max_length=10, blank=True, null=True) 
    services = models.ForeignKey(Services, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='rooms/',null=True)

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.name

class RoomPhoto(models.Model):
    description = models.CharField(max_length=100, blank=True)
    image1 = models.ImageField(upload_to='rooms/',null=True)
    room = models.ForeignKey(Rooms, related_name="room_photos", on_delete=models.CASCADE, blank=True, null=True)
   

    class Meta:
        verbose_name = 'Room  photo'
        verbose_name_plural = 'Room photos'
    
    def __str__(self):
        return self.room







    
     