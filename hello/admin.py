from django.contrib import admin

# Register your models here.
from .models import TodoList, Category, StoreFile


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class StoreFileAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "file")


admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(StoreFile, StoreFileAdmin)
