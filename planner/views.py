from django.shortcuts import render, redirect
from .forms import StudyTaskForm
from .models import StudyTask

def home(request):
    """Display the home page with a summary of saved tasks."""
    total_tasks = StudyTask.objects.count()
    total_minutes = sum(task.minutes for task in StudyTask.objects.all())
    context = {
        "total_tasks": total_tasks,
        "total_minutes": total_minutes,
    }
    return render(request, "planner/home.html", context)

def add_task(request):
    """Process user input and save a valid study task."""
    if request.method == "POST":
        form = StudyTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = StudyTaskForm()
    return render(request, "planner/add_task.html", {"form": form})

def task_list(request):
    """Retrieve saved tasks and display them dynamically."""
    tasks = StudyTask.objects.order_by("-created_at")
    return render(request, "planner/task_list.html", {"tasks": tasks})
