from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, AddCommentView, TaskDeleteView, TaskUpdateView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),  # Ensure this is correct
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('add/', TaskCreateView.as_view(), name='task_add'),
]