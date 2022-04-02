from cProfile import label
from typing import Tuple
from django import forms
from django.forms import ValidationError
from .models import Link

class LinkForm(forms.ModelForm):
    
    class Meta:
        model = Link
        fields = ['name', 'description', 'url']

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description.split()) < 3:
            raise ValidationError("Izoh kamida 3 ta so'zdan iborat bo'lishi kerak")
        
        return description
    
    def clean(self):
        super().clean()
        url_data = self.cleaned_data['url']
        if Link.objects.filter(url = url_data).exists():
            raise ValidationError('bunday havola mavjud')

        return self.cleaned_data

class RegisterForm(forms.Form):
    
    username = forms.CharField(max_length=120, required=True, label='Login')
    email = forms.EmailField(max_length=50, initial='example@gmail.com', 
            help_text="Iltimos to'g'ri email kiriting")
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    description = forms.CharField(max_length=5000, widget=forms.Textarea)

    def clean_password(self):
        parol = self.data['password']
        if len(parol) < 8:
            raise ValidationError("Parol uzunligi 8 tadan kam bo'lmasligi kerak")
        if parol.isnumeric():
            raise ValidationError("Parol faqat sondan iborat bo'lmasligi kerak")
        if parol.isalpha():
            raise ValidationError("Parol faqat harflardan iborat bo'lmasligi kerak")
        return parol
    
    def clean_confirm_password(self):
        parol = self.data['password']
        confirm_parol = self.data['confirm_password']
        if parol != confirm_parol:
            raise ValidationError("Tasdiqlash paroli noto'g'ri")
        return confirm_parol
    
