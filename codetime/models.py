from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=32, null=True)
	password = models.CharField(max_length=32, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	text1 = models.CharField(max_length=32, null=True)
	text2 = models.CharField(max_length=32, null=True)
	text3 = models.CharField(max_length=32, null=True)
	text4 = models.CharField(max_length=32, null=True)
	text5 = models.CharField(max_length=32, null=True)
	text6 = models.CharField(max_length=32, null=True)
	text7 = models.CharField(max_length=32, null=True)
	text8 = models.CharField(max_length=32, null=True)
	text9 = models.CharField(max_length=32, null=True)
	text10 = models.CharField(max_length=32, null=True)
	text11 = models.CharField(max_length=32, null=True)
	text12 = models.CharField(max_length=32, null=True)
	text13 = models.CharField(max_length=32, null=True)
	text14 = models.CharField(max_length=32, null=True)
	text15 = models.CharField(max_length=32, null=True)
	text16 = models.CharField(max_length=32, null=True)
	text17 = models.CharField(max_length=32, null=True)
	text18 = models.CharField(max_length=32, null=True)
	text19 = models.CharField(max_length=32, null=True)
	text20 = models.CharField(max_length=32, null=True)
	text21 = models.CharField(max_length=32, null=True)
	text22 = models.CharField(max_length=32, null=True)
	text23 = models.CharField(max_length=32, null=True)
	text24 = models.CharField(max_length=32, null=True)
	text25 = models.CharField(max_length=32, null=True)
	text26 = models.CharField(max_length=32, null=True)
	text27 = models.CharField(max_length=32, null=True)
	text28 = models.CharField(max_length=32, null=True)
	text29 = models.CharField(max_length=32, null=True)
	text30 = models.CharField(max_length=32, null=True)
	# 生产中 false 已完成 true
	status = models.BooleanField(default=False)
	# 未发货false 已发货 true
	shipments = models.BooleanField(default=False)
	# 未结款false 未结款 true
	knot = models.BooleanField(default=False)
	def __str__(self):
		return self.text1
	
		