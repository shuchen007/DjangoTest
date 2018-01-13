from django.contrib import admin

# Register your models here.
# Register your models here.
from hello.models import Test, Contact, Tag


# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    # fields = ('name', 'email')
    list_display = ('name', 'age', 'email')  # list
    search_fields = ('name',)#查询栏
    inlines = [TagInline]  # 内联(Inline)显示
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]
    )#输入栏分块显示，定义不同格式。


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])