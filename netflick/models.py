from django.db import models




class Show(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=15)
    description = models.TextField()
    year_released = models.IntegerField()