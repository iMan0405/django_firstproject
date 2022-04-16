
from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.forms import ValidationError

class LoginForm(forms.Form):

    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise ValidationError('Bunday foydalanuvchi mavjud emas')
        return username
    
    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data['password']
        if username:
            user = User.objects.filter(username=username).first()
            if user:
                if not user.check_password(password):
                    raise ValidationError("Parol noto'g'ri")
        return password


class RegisterForm(forms.Form):
    
    email = forms.EmailField(max_length=120, required=True, label='Elektron pochta')
    password = forms.CharField(max_length=100, label='Parol',
                            widget=forms.PasswordInput(attrs={'class':'special'}))
    confirm_password = forms.CharField(max_length=100, label='Parolni tasdiqlash', 
                            widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name':'Ism',
            'last_name':'Familiya'
        }

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
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Ushbu email sistemada ro'yxatdan o'tgan")
        return email