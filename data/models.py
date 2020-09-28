from django.db import models


class Information(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    cr_date = models.DateField(auto_now_add=True)
    cr_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
