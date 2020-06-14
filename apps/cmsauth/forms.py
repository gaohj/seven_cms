from django import forms
from django.core import validators
from apps.forms import FromMixin
from .models import User
from django.core.cache import cache
class LoginForm(forms.Form,FromMixin):
    telephone = forms.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3-8]\d{9}',message='请输入正确的手机号')])
    password = forms.CharField(max_length=30,min_length=6,error_messages={"max_length":"密码最多不能超过30个字符","min_length":"最短不能少于6个字符"})
    remember = forms.IntegerField(required=False)

class RegisterForm(forms.Form,FromMixin):
    telephone = forms.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3-8]\d{9}',message='请输入正确的手机号')])
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=30,min_length=6,error_messages={"max_length":"密码最多不能超过30个字符","min_length":"最短不能少于6个字符"})
    password2 = forms.CharField(max_length=30,min_length=6,error_messages={"max_length":"密码最多不能超过30个字符","min_length":"最短不能少于6个字符"})
    image_captcha = forms.CharField(max_length=5,min_length=5)
    sms_captcha = forms.CharField(max_length=5,min_length=5)


    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('两次密码输入不一致')

        image_captcha = cleaned_data.get('image_captcha')
        catch_image_captcha = cache.get(image_captcha.lower())
        print(catch_image_captcha)
        if not catch_image_captcha or catch_image_captcha.lower() != image_captcha.lower():
            raise forms.ValidationError('图形验证码有误')

        telephone = cleaned_data.get('telephone')
        existes = User.objects.filter(telephone=telephone).exists()
        if existes:
            raise forms.ValidationError('该手机号已经存在')

        return cleaned_data

