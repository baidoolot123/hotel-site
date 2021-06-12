from django.db import models

# Create your models here.
class RoomCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Категория номера'
        verbose_name_plural = 'Категории номеров'

class Rooms(models.Model):
    room_number = models.IntegerField(blank=True, null=True)
    room_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photos = models.ImageField(upload_to='room_images', blank=True)
    room_type = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    booked = models.BooleanField()

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'
    
    def __str__(self):
        return self.room_name



    
     