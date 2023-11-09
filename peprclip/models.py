from django.db import models
from django.utils import timezone


# Create your models here.
# 当前假设模型服务是通过Django包裹做成服务，然后在docker上暴露一个调用接口的微服务架构，那么当前主业务的表单应该是一个功能列表。
class peprclip_function(models.Model):
    #功能名称
    function_name = models.CharField(max_length=100)
    #功能简介
    function_info = models.TextField()
    #输入介绍
    function_input_intro = models.TextField()
    #输出介绍
    function_output_intro = models.TextField()
    #创建时间
    created = models.DateTimeField(default=timezone.now)
    #更新时间
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.function_name
