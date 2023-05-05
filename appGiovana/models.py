from django.db import models

class Dogs(models.Model):
  title= models.CharField(max_length=50)
  raca= models.CharField(max_length=30)
  idade= models.CharField(max_length=30)
  adoção= models.DateField()

class Metas(models.Model):
  title = models.CharField(max_length = 50)
  description = models.TextField()
  place= models.CharField(max_length = 50)
  done=models.BooleanField()
