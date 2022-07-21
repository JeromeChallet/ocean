from django.db import models

class School2(models.Model):
    name = models.CharField(max_length=80)
    phone = models.IntegerField()
    headteacher = models.CharField(max_length=100)


class Addaschool(models.Model):
    schoolname = models.CharField(max_length=80)
    schoolphone = models.CharField(max_length=15)
    schoolfax = models.CharField(max_length=15)

    companyname = models.CharField(max_length=80)
    postelcode = models.CharField(max_length=8)
    addressone = models.CharField(max_length=100)
    addresstwo = models.CharField(max_length=100)
    googlemaplink = models.CharField(max_length=100)
    trainstation = models.CharField(max_length=100)
    busstation = models.CharField(max_length=100)
    ownername = models.CharField(max_length=30)
    ownerphone = models.CharField(max_length=15)
    personincharge = models.CharField(max_length=30)
    picphone = models.CharField(max_length=15)
