from django.shortcuts import render
from django.core.cache import cache
from user.logic import get_code


# Create your views here.

def get_verify_code(request):
    '''手机注册'''
    
    code = get_code()
    cache.set('VerifyCode-%s' %phonenumber, code)

def login(request):
    '''短信验证码登录'''
    request.POST.get(phonenumber)
    cache.get('VerifyCode-%s')

def get_profile(request):
    '''获取个人资料'''
    pass

def modify_profile(request):
    '''修改个人资料'''
    pass

def upload_avatar(request):
    '''上传头像'''
    pass


