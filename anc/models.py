from django.db import models

class Students(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=30)
    s_year = models.IntegerField()
    s_sec = models.CharField(max_length=1)
    s_dep = models.CharField(max_length=30)
    password = models.CharField(max_length=32, null=True)


