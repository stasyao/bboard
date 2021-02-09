from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    list_display = [
        'email',
        'phone_number',
        'last_name',
        'first_name',
        'middle_name',
        'role',
        'call_reception_time',
        'is_active',
        'uuid',
    ]
    # Кастомизированный набор полей для add user (иначе требует username)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': list_display + ['password1', 'password2', ],
        }
        ),
    )
    fieldsets = (
        (None, {'fields': list_display}),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(get_user_model(), CustomUserAdmin)
