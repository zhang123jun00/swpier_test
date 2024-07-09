from django.shortcuts import render
from django.core.cache import cache
from user.logic import get_code
from lib.http import render_json


# Create your views here.

def get_verify_code(request):
    '''手机注册'''
    phonenumber = request.POST.get('phonenumber')
    code = get_code()
    cache.set('VerifyCode-%s' %phonenumber, code)
    return render_json(code, 0)

def login(request):
    '''短信验证码登录'''
    # request.POST.get(phonenumber)
    # cache.get('VerifyCode-%s')
    pass

def get_profile(request):
    '''获取个人资料'''
    pass

def modify_profile(request):
    '''修改个人资料'''
    pass

def upload_avatar(request):
    '''上传头像'''
    pass


