from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    class Meta:
        model = Listing
    list_display = ['id', 'title', 'address', 'city', 'price', 'realtor', 'is_published']
    list_display_links = ['id', 'title']
    list_filter = ('realtor__name',)
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'city', 'price', )
    list_per_page = 2

    def get_realtor(self, obj):
        return obj.realtor.name
    get_realtor.short_description = 'Realtor'
admin.site.register(Listing, ListingAdmin)
