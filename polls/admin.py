from django.contrib import admin
from .models import Customer, Login, Course

admin.site.register(Login)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'mob', 'email']


@admin.register(Course)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc','duration']
