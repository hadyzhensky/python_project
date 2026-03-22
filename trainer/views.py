from django.shortcuts import render, get_object_or_404
from .models import SQLTask, HistoricalEvent
from django.db import connection

def task_detail(request, task_id):
    task = get_object_or_404(SQLTask, id=task_id)
    all_tasks = SQLTask.objects.all()
    sample_data = HistoricalEvent.objects.all()[:10]

    result = None
    error = None
    is_correct = None
    columns = None

    prev_task = SQLTask.objects.filter(id__lt=task.id).order_by('-id').first()
    next_task = SQLTask.objects.filter(id__gt=task.id).order_by('id').first()

    if request.method == "POST":
        user_query = request.POST.get("query").strip()
        if not user_query.startswith("select"):
            error = "Ошибка! Разрешены только SELECT запросы"
        else:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(user_query)
                    columns = [col[0] for col in cursor.description]
                    result = cursor.fetchall()
                print(result)
                # проверка
                with connection.cursor() as cursor:
                    cursor.execute(task.correct_query)
                    correct_result = cursor.fetchall()
                print(correct_result)
                # приводим всё к строкам и нижнему регистру
                result_str = [[str(c).lower() for c in row] for row in result]
                correct_str = [[str(c).lower() for c in row] for row in correct_result]

                # сортируем строки, чтобы порядок не влиял
                is_correct = (sorted(result_str) == sorted(correct_str))

            except Exception as e:
                error = str(e)

    return render(request, 'trainer/task.html', {
        'task': task,
        'data': sample_data,
        'all_tasks': all_tasks,
        'result': result,
        'error': error,
        'is_correct': is_correct,
        'prev_task': prev_task,
        'next_task': next_task,
        'columns': columns
    })