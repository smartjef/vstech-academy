from django.contrib import admin
from .models import Subject, Comments, Course, Module

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title','slug','created','updated']
    prepopulated_fields = {'slug':('title',)}

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','subject','owner','image','price','created']
    list_filter = ['created','subject','owner','price']
    search_fields = ['title','overview', 'price']
    prepopulated_fields = {'slug':('title',)}
    inlines = [ModuleInline]