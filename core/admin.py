from django.contrib import admin

from core.models import User, Customer, PlayerSale


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'is_admin',
        'is_active',
    )


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'balance',
        'is_active',
    )
    readonly_fields = (
        'balance',
        'user',
    )

    def has_add_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        obj.user.is_active = obj.is_active
        obj.user.save()
        super().save_model(request, obj, form, change)


class PlayerSaleAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'kind',
        'value',
        'date_added',
    )
    readonly_fields = (
        'kind',
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        customer = obj.customer
        customer.update_balance(value=obj.value)


admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(PlayerSale, PlayerSaleAdmin)
