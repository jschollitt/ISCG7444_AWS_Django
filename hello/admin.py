from django.contrib import admin

# Register your models here.
from .models import TodoList, Category


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Category, CategoryAdmin)
