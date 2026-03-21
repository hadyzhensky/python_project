from .models import SQLTask
from django.shortcuts import render, redirect, get_object_or_404
from .models import SQLTask
from django.contrib import messages
from django.db import connection

def task_list(request):
    tasks = SQLTask.objects.all()  # берем все задачи из базы
    return render(request, 'trainer/task_list.html', {'tasks': tasks})

def check_sql(request, task_id):
    task = get_object_or_404(SQLTask, id=task_id)
    if request.method == 'POST':
        user_query = request.POST.get('query')
        if user_query.strip() == task.correct_query.strip():
            messages.success(request, "Верно! ✅")
        else:
            messages.error(request, "Неверно ❌")
    return redirect('task_list')