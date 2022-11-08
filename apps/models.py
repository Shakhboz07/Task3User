from django.db import models
from django.db.models import TextChoices


# Create your models here.


class User(models.Model):
    class TimeChoice(TextChoices):
        FULL_TIME = 'Full-time'
        PART_TIME = 'Part-time'

    class CityChoice(TextChoices):
        TORONTO = 'Toronto, CAN'
        NEW_YORK = 'New York, US'
        MUMBAI = 'Mumbai, IN'

    picture = models.ImageField(upload_to='user/')
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)
    time = models.CharField(max_length=55, choices=TimeChoice.choices, default=TimeChoice.FULL_TIME)
    address = models.CharField(max_length=55, choices=CityChoice.choices, default=CityChoice.NEW_YORK)
    price = models.IntegerField()
    field_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title


