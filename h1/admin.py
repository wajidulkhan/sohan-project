from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','reg','dep'] 