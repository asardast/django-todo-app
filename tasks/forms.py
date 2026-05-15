from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title'] # فقط فیلد عنوان رو برای اضافه کردن می‌خوایم

        