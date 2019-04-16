from django.db import models

# Create your models here.


class Games(models.Model):
    gamename = models.CharField(max_length=20)
    company = models.CharField(max_length=10)
    issue_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gamename


class Protagonist(models.Model):
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    undergo = models.CharField(max_length=200)

    def __str__(self):
        return self.name


