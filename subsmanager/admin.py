from django.contrib import admin
from .models import Sub, Custom


# Register your models here

# @admin.register(Sub)
# @admin.register(Custom)
admin.site.register(Sub)
admin.site.register(Custom)
