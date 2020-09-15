from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Greeting, TodoList, Category


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def list(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":

        if "taskAdd" in request.POST:
            title = request.POST["description"]
            email = request.POST["email"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = title + " -- " + date + " " + category
            Todo = TodoList(title=title, content=content, email=email, due_date=date, category=Category.objects.get(name=category))
            Todo.save()
            return redirect("/list/")

        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()

    return render(request, "list.html", {"todos": todos, "categories":categories})
