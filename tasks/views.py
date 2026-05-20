""" from django.shortcuts import render, redirect
from .models import Task # مدل تسک را وارد می‌کنیم
from .forms import TaskForm

def home_view(request):
    # گرفتن تمام اطلاعات از جدول Task در دیتابیس
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() # ذخیره در دیتابیس
            return redirect('/') # صفحه رو رفرش کن تا تسک جدید رو ببینی

    context = {'tasks': tasks, 'form': form}
    
    # فرستادن اطلاعات به قالب HTML تحت نام 'tasks'
    return render(request, 'tasks/list.html', {'tasks': tasks, 'form': form})

def delete_task(request, pk):
    task = Task.objects.get(id=pk) # تسک مورد نظر رو بر اساس آی‌دی پیدا کن
    task.delete() # حذفش کن!
    return redirect('/') # دوباره برگرد به صفحه اصلی

def complete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed # وضعیت رو معکوس کن
    task.save()
    return redirect('/') """

from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer