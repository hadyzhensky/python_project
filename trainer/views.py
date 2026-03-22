from django.shortcuts import render, redirect, get_object_or_404
from .models import SQLTask, HistoricalEvent, UserProgress
from django.db import connection
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'trainer/home.html')

@login_required
def task_list_view(request):
    tasks = SQLTask.objects.all()
    completed_task_ids = UserProgress.objects.filter(
        user=request.user, 
        is_completed=True
    ).values_list('task_id', flat=True)
    
    return render(request, 'trainer/task_list.html', {
        'tasks': tasks,
        'completed_task_ids': completed_task_ids
    })

@login_required
def profile_view(request):
    total_tasks = SQLTask.objects.count()
    completed_tasks = UserProgress.objects.filter(user=request.user, is_completed=True).count()
    remaining_tasks = total_tasks - completed_tasks
    percent = int(completed_tasks / total_tasks * 100) if total_tasks else 0

    completed_list = UserProgress.objects.filter(user=request.user, is_completed=True)
    return render(request, 'trainer/profile.html', {
        'total': total_tasks,
        'completed': completed_tasks,
        'remaining': remaining_tasks,
        'percent': percent,
        'completed_list': completed_list
    })

@login_required
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
                if is_correct:
                    UserProgress.objects.get_or_create(user=request.user, task=task, defaults={'is_completed': True})

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

@login_required
def progress_view(request):
    total_tasks = SQLTask.objects.count()
    completed_tasks = UserProgress.objects.filter(user=request.user, is_completed=True).count()
    percent = int(completed_tasks / total_tasks * 100) if total_tasks else 0

    completed_list = UserProgress.objects.filter(user=request.user, is_completed=True)
    return render(request, 'trainer/progress.html', {
        'total': total_tasks,
        'completed': completed_tasks,
        'percent': percent,
        'completed_list': completed_list
    })

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # редирект на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'trainer/signup.html', {'form': form})