from django.contrib import admin
from .models import User

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'first_name')  # Fields to display in the list view
    search_fields = ('email', 'phone', 'first_name')  # Fields to add search functionality
    list_filter = ('first_name',)  # Fields to filter in the list view
    
admin.site.register(User, UsersAdmin)
