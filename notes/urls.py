from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, AddCommentView, TaskDeleteView, TaskUpdateView, CommentUpdateView, CommentDeleteView, LikeCommentView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),  # Ensure this is correct
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('add/', TaskCreateView.as_view(), name='task_add'),
    path('<int:pk>/comment/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('<int:pk>/comment/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    path('<int:pk>/comment/like/', LikeCommentView.as_view(), name='like_comment'),
]