from django.contrib import admin
from .models import Advertisement

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display =['title', 'description', 'price', 'created_date', 'updated_date', 'category', 'author', 'location', 'auction']
    list_filter = ['price', 'created_at', 'updated_at', 'category']
    actions = ['forbid_the_auction', 'permit_the_auction']
    fieldsets = (
        ('Общее', {
            'fields' : ('title', 'description', 'category', 'author', 'location')
        }),
        ('Финансы', {
            'fields' : ('price', 'auction'),
            'classes' : ['collapse']
        })
    )

    @admin.action(description="Убрать возможность торга.")
    def forbid_the_auction(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга.")
    def permit_the_auction(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)