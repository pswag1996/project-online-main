from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser

# admin.site.register(CustomUser, CustomUserAdmin)


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(File)
# admin.site.register(CustomUser)
