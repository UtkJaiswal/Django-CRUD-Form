from django.db import models

# Create your models here.
from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    