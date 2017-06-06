from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=32, null=True)
	password = models.CharField(max_length=32, null=True)

	def __str__(self):
		return self.name