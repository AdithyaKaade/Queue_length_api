from django.contrib import admin
from .models import Logdata_put
# Register your models here.
class LogDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(Logdata_put, LogDataAdmin)