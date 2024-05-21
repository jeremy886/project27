from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # add_fieldsets defines the layout of fields for the add (create) view of the user model
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Extra Info", {'fields': ('age',)}),
    )

    # fieldsets defines the layout of fields for the change (edit) view of the user model.
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
