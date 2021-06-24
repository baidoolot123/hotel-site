from django.db import models

# Create your models here.

class About(models.Model):
    mission = models.TextField()
    vision = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return str(self.id)
