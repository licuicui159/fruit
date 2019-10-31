from django.contrib import admin
from .models import *
# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    #列表页 数据显示字段
    list_display = ('title', 'goodsType', 'price', 'spec', 'isActive')
    list_filter = ('goodsType','isActive')
    search_fields = ('title',)
    list_editable = ('price', 'spec')

admin.site.register(GoodsType)
admin.site.register(Goods, GoodsAdmin)