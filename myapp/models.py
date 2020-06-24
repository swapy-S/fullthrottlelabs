from django.db import models
from django.urls import reverse

# Create your models here.
class UserData(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse("myapp:api")
    def __str__(self):
        return str(self.id + " " + self.real_name)


class Activity(models.Model):
    user = models.ForeignKey(
        UserData, related_name="activity_periods", on_delete=models.CASCADE
    )
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("myapp:api")

    def __str__(self):
        return str(self.user.real_name)
