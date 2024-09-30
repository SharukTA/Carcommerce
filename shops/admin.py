from django.contrib import admin
from .models import Shopowner

@admin.register(Shopowner)
class ShopOwnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'shopname', 'ownername', 'phone', 'address', 'license_certificate', 'is_approved','rejected')
    list_filter = ('is_approved','rejected')

    actions = ['approve_shops', 'reject_shops']

    def approve_shops(self, request, queryset):
        count = queryset.update(is_approved=True,reject=False)
        self.message_user(request, f'{count} shop(s) approved.')

    def reject_shops(self, request, queryset):
        count=0
        for shopowner in queryset:
            shopowner.reject=True
            shopowner.save()
            user=shopowner.user
            shopowner.delete()
            user.delete()
            count+=1
        self.message_user(request, f'{count} shopowner(s) rejected and removed.')

    approve_shops.short_description = 'Approve selected shopowners'
    reject_shops.short_description = 'Reject and remove selected shopowners'


