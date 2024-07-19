from django.db import models

# Create your models here.
class help(models.Model):


    Name = models.CharField(max_Length=122)
    Lname = models.CharField(max_Length=122)  
    Email = models.CharField(max_Length=122)
    Comm = models.TextField()
    date = models.DateField()
    
