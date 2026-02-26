from django.contrib.admin import ModelAdmin


class BaseAdmin(ModelAdmin):
    readonly_fields = ('created_at', 'updated_at','id')