from django.db import models

class Price_Gold(models.Model):
    P1 = models.SmallIntegerField()
    P2 = models.SmallIntegerField()
    P3 = models.SmallIntegerField()
    P4 = models.SmallIntegerField()
    P5 = models.SmallIntegerField()
    P6 = models.SmallIntegerField()
    P7 = models.SmallIntegerField()
    P8 = models.SmallIntegerField()
    P9 = models.SmallIntegerField()
    P10 = models.SmallIntegerField()
    P11 = models.SmallIntegerField()
    P12 = models.SmallIntegerField()
    P13 = models.SmallIntegerField()
    P14 = models.SmallIntegerField()
    P15 = models.SmallIntegerField()
    P16 = models.SmallIntegerField()
    P17 = models.SmallIntegerField()
    P18 = models.SmallIntegerField()
    P19 = models.SmallIntegerField()
    P20 = models.SmallIntegerField()

class Data_Gold(models.Model):
    Csv_File = models.FileField(upload_to="uploads/")
