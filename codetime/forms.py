from django import forms
class NameForm(forms.Form):
	name = forms.CharField(label='name', max_length=100)
	pasword = forms.CharField(label='password')
