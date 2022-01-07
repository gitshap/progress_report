from django.contrib import admin
from reports.models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')


admin.site.register(Report)
