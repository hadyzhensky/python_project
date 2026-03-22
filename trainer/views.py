from django.shortcuts import render, redirect, get_object_or_404
from .models import SQLTask, HistoricalEvent
from django.contrib import messages
from django.db import connection

def task_detail(request, task_id):
    task = get_object_or_404(SQLTask, id=task_id)

    # просто пример данных (10 строк)
    sample_data = HistoricalEvent.objects.all()[:10]

    return render(request, 'trainer/task.html', {
        'task': task,
        'data': sample_data
    })