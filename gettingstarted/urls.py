from django.urls import path
from django.conf.urls import url
from django.contrib import admin
import hello.views

admin.autodiscover()


urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("list/", hello.views.list, name="TodoList"),
]
