from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Department, Designation, Branch, Employee, CustomUser
from .forms import SignUpForm, UserUpdateForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = UserUpdateForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Branch)
admin.site.register(Employee)
admin.site.register(CustomUser, CustomUserAdmin)