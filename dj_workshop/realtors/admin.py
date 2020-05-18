from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    class Meta:
        model = Realtor
    list_display = ['id', 'name', 'email', 'phone', 'message', 'contact_date', 'is_mvp']
    list_display_links = ['id', 'name', 'phone']
    list_filter = ('name',)
    list_editable = ['is_mvp']
    search_fields = ('name', 'email', 'phone',)
    list_per_page = 5
# Register your models here.
admin.site.register(Realtor, RealtorAdmin)
