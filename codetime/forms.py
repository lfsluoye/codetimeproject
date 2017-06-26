from django import forms
from .models import Person
from django.core.exceptions import ValidationError

class LoginForm(forms.ModelForm):
	# name = forms.CharField(label='name', max_length=100)
	# pasword = forms.CharField(label='password')

	# def clean_name(self):
	# 	value = self.clean_data.get('name')
	# 	try:
	# 		Person.objects.get(name=value)
	# 		raise ValidationError("%s的信息已存在" % value)
	# 	except Person.DoesNotExist:
	# 		pass
	# 	return value
	# def clean(self):
	# 	clean_data = super(LoginForm, self).clean()
	# 	value = clean_data.get('name')
	# 	try:
	# 		Person.objects.get(name=value)
	# 		self._errors['name'] = self.error_class(['"%s的信息已存在" % value'])
	# 	except Person.DoesNotExist:
	# 		pass
	# 	return clean_data
	class Meta:
		model = Person
		exclude = ('id',)
