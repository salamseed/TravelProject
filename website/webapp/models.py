from django.db import models

class whychooseus(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()

class meet_the_team(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()

