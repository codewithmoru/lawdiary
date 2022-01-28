from django.db import models

# Create your models here.
class Users(models.Model):
    PrevD = models.DateField()
    CourtName = models.TextField(max_length=200)
    CaseNo = models.TextField(max_length=200)
    Names = models.TextField(max_length=200)
    Position = models.TextField(max_length=12)
    NextD = models.DateField()
    def __str__(self):
       return self.Names
