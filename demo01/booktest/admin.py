from django.contrib import admin
from .models import BookInfo,HeroInfo

# Register your models here.


# 关联注册类
class HreoInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['bookname']
    inlines = [HreoInfoInline]


admin.site.register(BookInfo, BookInfoAdmin)


# 重写HeroInfo的后台管理类:
class HeroInfoAdmin(admin.ModelAdmin):
    # 显示列表中的列名
    list_display = ['name', 'gender', 'wu']
    # 显示过滤
    list_filter = ['hname', 'hgender']
    # 显示搜索
    search_fields = ['hname', 'hconent', 'hbook']
    # 显示分页
    list_per_page = 5


admin.site.register(HeroInfo,HeroInfoAdmin)






"""
通过少量的代码实现强大的后台功能
"""
