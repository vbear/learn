#coding=utf8
from django.contrib import admin

# Register your models here.
#by vbear
from models import BookInfo,HeroInfo


#显示表格里面的标题
#list_display 显示字段
#list_filter 过滤字段
#search_fields 搜索字段
#list_per_page 分页
#list_editable 设置可以编辑
# class BookInfoAdmin(admin.ModelAdmin):
#     list_display = ['bpub_date','btitle']
#     search_fields= ['btitle']

def gender(self):
    if self.hgender:
        return '男'
    else:
        return '女'
gender.short_description='性别'

class HeroInfoAdmin(admin.ModelAdmin):
    list_display= ['id','hname',gender,'hcontent']

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 4

class BookInfoAdmin(admin.ModelAdmin):
    inlines = [HeroInfoInline]
    list_display = ['bpub_date', 'btitle']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)

