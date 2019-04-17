from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.btitle

    def bookname(self):
        return self.btitle
    bookname.short_description = '书名'


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hconent = models.CharField(max_length=100)
    # 外键 第一个参数为表名，第二个参数代表删除类型
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.hname

    def name(self):
        return self.hname
    name.short_description = '主角'

    def gender(self):
        return self.hgender
    gender.short_description = '性别'

    def wu(self):
        return self.hconent
    wu.short_description = '武功、经历'


"""

ORM 对象中 O
需要在这里定义实体类

"""
