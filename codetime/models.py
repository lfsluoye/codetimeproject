from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=32, null=True, unique=True)
	password = models.CharField(max_length=32, null=True)
	userLimit_choice = (
		(0, '超级用户'),
		(1, '普通员工'),
		(2, '编外人员'),
	)
	userlimitid = models.IntegerField(choices=userLimit_choice, default=0, blank=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	userId = models.ForeignKey('Person', default = 1, editable=False, on_delete=models.CASCADE)
	text1 = models.CharField(max_length=32, null=True)
	text2 = models.CharField(max_length=32, blank=True, default="")
	text3 = models.CharField(max_length=32, null=True)
	text4 = models.CharField(max_length=32, null=True)
	text5 = models.CharField(max_length=32, null=True)
	text6 = models.CharField(max_length=32, null=True)
	text7 = models.CharField(max_length=32, null=True)
	text8 = models.CharField(max_length=32, null=True)
	text9 = models.CharField(max_length=32, null=True)
	text10 = models.CharField(max_length=32, blank=True, default="")
	text11 = models.CharField(max_length=32, blank=True, default="")
	text12 = models.CharField(max_length=32, blank=True, default="")
	text13 = models.CharField(max_length=32, blank=True, default="")
	text14 = models.CharField(max_length=32, blank=True, default="")
	text15 = models.CharField(max_length=32, blank=True, default="")
	text16 = models.CharField(max_length=32, blank=True, default="")
	text17 = models.CharField(max_length=32, blank=True, default="")
	text18 = models.CharField(max_length=32, blank=True, default="")
	text19 = models.CharField(max_length=32, blank=True, default="")
	text20 = models.CharField(max_length=32, blank=True, default="")
	text21 = models.CharField(max_length=32, blank=True, default="")
	text22 = models.CharField(max_length=32, blank=True, default="")
	# 下单时间
	text23 = models.CharField(max_length=32, null=True)
	# 交货日期
	text24 = models.CharField(max_length=32, null=True)
	text25 = models.CharField(max_length=32, blank=True, default="")
	text26 = models.CharField(max_length=32, blank=True, default="")
	text27 = models.CharField(max_length=32, blank=True, default="")
	text28 = models.CharField(max_length=32, blank=True, default="")
	text29 = models.CharField(max_length=32, blank=True, default="")
	text30 = models.CharField(max_length=32, blank=True, default="")
	# 生产中 false 已完成 true
	status = models.BooleanField(default=False)
	# 未发货false 已发货 true
	shipments = models.BooleanField(default=False)
	# 未结款false 未结款 true
	knot = models.BooleanField(default=False)
	def __str__(self):
		return self.text1

