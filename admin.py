from django.contrib import admin
from .models import guest

# Register your models here.
@admin.register(guest)
class guestAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phone','messages']
    