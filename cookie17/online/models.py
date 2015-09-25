from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)

    def __unicode__(self):
	return self.username
