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
	userId = models.CharField(max_length=32, blank=True, default="", editable=False)
	# 客户
	text1 = models.CharField(max_length=32, null=True)
	# 地址
	text2 = models.CharField(max_length=32, blank=True, default="")
	# 合同编号 订单号
	text3 = models.CharField(max_length=32, blank=True, default="", editable=False)
	# 单价
	text4 = models.DecimalField(max_digits=10, decimal_places=3,default=0)
	#总金额
	amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
	# 产品名称
	text5 = models.CharField(max_length=32, null=True)
	# 尺寸
	text6 = models.CharField(max_length=32, blank=True, default="")
	# 颜色
	text7 = models.CharField(max_length=32, blank=True, default="")
	# 成品数量
	text8 = models.PositiveIntegerField(default=0)
	text9 = models.CharField(max_length=32, blank=True, default="")
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
	# 菲林编号
	text21 = models.CharField(max_length=32, blank=True, default="")
	# 刀版编号
	text22 = models.CharField(max_length=32, blank=True, default="")

	# 下单时间
	text23 = models.CharField(max_length=32, null=True)
	# 交货日期
	text24 = models.CharField(max_length=32, blank=True, default="")
	# 印刷版长
	text25 = models.CharField(max_length=32, blank=True, default="")
	# 生产印数
	# product_printing_number = models.CharField(max_length=32, blank=True, default="")
	# 生产印数
	text26 = models.CharField(max_length=32, blank=True, default="")
	text27 = models.CharField(max_length=32, blank=True, default="")
	text28 = models.CharField(max_length=32, blank=True, default="")
	text29 = models.CharField(max_length=32, blank=True, default="")
	text30 = models.CharField(max_length=32, blank=True, default="")
	text31 = models.CharField(max_length=32, blank=True, default="")
	# 留样
	retention_samples = models.CharField(max_length=32, blank=True, default="")
	# 生产中 false 已完成 true
	status = models.BooleanField(default=False)
	# 未发货false 已发货 true
	shipments = models.BooleanField(default=False)
	# 未结款false 未结款 true
	knot = models.BooleanField(default=False)
	def __str__(self):
		return self.text1

