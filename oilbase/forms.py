from django import forms
from .models import CallBack

class CallBackForm(forms.ModelForm):

	class Meta:
		model = CallBack
		fields = ('name', 'phone', 'email', 'message',)
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control',  'placeholder':'Ваше имя', 'required': True}),
			'phone': forms.TextInput(attrs={'class':'form-control',  'placeholder':'Ваш телефон', 'required': True}),
			'email': forms.EmailInput(attrs={'class':'form-control',  'placeholder':'Ваш почтовый адрес', 'required': True}),
			'message': forms.Textarea(attrs={'class':'form-control',  'placeholder':'Ваше сообщение', 'rows':'6', 'required': True})
		}