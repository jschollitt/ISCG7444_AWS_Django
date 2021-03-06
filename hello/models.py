from django.db import models
from django.utils import timezone


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    email = models.EmailField(max_length=200, blank=True)
    created = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, default="general", on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
