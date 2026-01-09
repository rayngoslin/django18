from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django import forms
from .models import Task, Comment  # Remove Note, keep Task
from django.contrib.auth.forms import UserCreationForm

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'notes/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        priority = self.request.GET.get('priority')
        deadline = self.request.GET.get('deadline')

        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)
        if deadline:
            queryset = queryset.filter(deadline=deadline)

        return queryset

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'notes/note_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'notes/task_form.html'
    fields = ['title', 'description', 'status', 'priority', 'deadline']
    success_url = reverse_lazy('task_list')

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'notes/task_form.html'  # Reuse the same form template
    fields = ['title', 'description', 'status', 'priority', 'deadline']
    success_url = reverse_lazy('task_list')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'notes/task_confirm_delete.html'  # Create this template
    success_url = reverse_lazy('task_list')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class AddCommentView(LoginRequiredMixin, FormView):
    template_name = 'notes/add_comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        task = Task.objects.get(pk=self.kwargs['pk'])
        form.instance.task = task
        form.instance.author = self.request.user
        form.save()
        return redirect('task_detail', pk=task.pk)