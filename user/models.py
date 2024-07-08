import datetime
from django.db import models

# Create your models here.

class User(models.Model):
    '''用户数据模型'''
    sex = (
        ('0', '男'),
        ('1', '女')
    )
    nickname = models.CharField(max_length=32,
                                unique=True)
    phonenumber = models.CharField(max_length=16,
                                   unique=True)
    sex = models.CharField(max_length=8,
                           choices=sex,
                           default=0)
    birth_year= models.IntegerField(default=1990)
    birth_month= models.IntegerField(default=3)
    birth_day= models.IntegerField(default=4)
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)

    @property
    def age(self):
        now = datetime.date.today()
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        return (now - birth_date).days // 365
    
    @property
    def profile(self):
        '''用户得配置项'''
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile


class Profile(models.Model):
    '''用户配置项'''
    sex = (
        ('0', '男'),
        ('1', '女')
    )
    dating_sex = models.CharField(default=1,
                                  choices=sex,
                                  verbose_name='匹配性别',
                                  max_length=8)
    location = models.CharField(max_length=32,
                                 verbose_name='目标城市')
    min_distance = models.IntegerField(default=1,
                                    verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10,
                                    verbose_name='最大查找范围')
    min_dating_age = models.IntegerField(default=18,
                                      verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=45,
                                      verbose_name='最大交友年龄')
    
    vibration = models.BooleanField(verbose_name='是否开启震动',
                                    default=True)
    only_matche = models.BooleanField(default=True,
                                    verbose_name='不让匹配的人看我的相册')
    auto_play = models.BooleanField(default=True,
                                 verbose_name='自动播放 ')