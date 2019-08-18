#创建虚拟环境
virtualenv E:\python\dailyfresh

#进入虚拟目录
e:\pythonenv\dailyfresh\Scripts>activate.bat

#创建项目
django-admin startproject dailyfresh
django-admin startproject dailyfresh

#安装django
pip install django==1.8.2

#检查是否成功
import django
django.get_version()


#创建应用
python manage.py startapp booktest

#生成数据
先创建models定义好字段，然后执行
python manage.py makemigrations
python manage.py migrate

#调试
python manage.py shell
from booktest.models import BookInfo,HeroInfo
from django.utils import timezone
from datetime import *

*所有数据
 BookInfo.objects.all()
 
*新建图书
b=BookInfo()
b.btitle='python'
b.bpub_date=datetime(year=2018,month=8,day=4)
b.save

*查找图书
b=BookInfo.objects.get(pk=1)

#创建用户
python manage.py createsuperuser

