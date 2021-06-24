from django.db import models

ROOM_TYPE = (
    ('double', 'DOUBLE'),
    ('twin', 'TWIN'),
    ('ben in a hostel', 'BED IN A HOSTEL'),
    ('studio', 'STUDIO'),
)

class Reservation(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.IntegerField()
    email = models.EmailField()
    # room_type = models.CharField(max_length=15, choices=ROOM_TYPE, default = 'double')
    notes = models.TextField()

    def __str__(self):
        return self.name 