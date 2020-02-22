from django.db import models
from datetime import timedelta
from django.conf import settings
import itertools as it
from django.contrib.auth.models import User

categories = (
    ('training','Training'),
    ('tournament','Tournament'),
    ('social','Social Event'),
    ('orga','Organization Event'),
    ('other','Other')
)

class Location(models.Model):
    name = models.CharField(max_length = 50)
    street = models.CharField(max_length = 100)
    place = models.CharField(max_length = 100)
    def __str__(self):
        return self.name


# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    category = models.CharField(choices = categories,max_length = 20, default = 'Training')
    date = models.DateTimeField()
    description = models.TextField(null = True)
    # date_end = models.DateTimeField(default = date + timedelta(hours = 2))
    location = models.ForeignKey('Location', on_delete=models.PROTECT,
                                 null = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.PROTECT)
    visibility = models.CharField(max_length=20,default='public')

    def __str__(self):
        return self.name

class PartChoice(models.Model):
    choice = models.CharField(max_length = 1)
    choicetext = models.CharField(max_length=20)

    def __str__(self):
        return self.choicetext


class Participation(models.Model):

    id = models.AutoField(primary_key=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE,)
    person = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.PROTECT)
    part = models.ForeignKey('PartChoice', on_delete=models.PROTECT,
                             related_name="party", null = True)

    def __str__(self):
        return str(self.id)
