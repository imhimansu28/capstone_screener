from django.contrib import admin

from .models import Company


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'company_name', 'company_code',)
    list_filter = ('company_group', 'company_industry')
    search_fields = ('company_name', 'company_code')
    ordering = ('company_name',)
    list_per_page = 25




admin.site.register(Company, CompanyAdmin)
