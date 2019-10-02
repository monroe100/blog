from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView


urlpatterns = [
    path('', PostListView.as_view(), name='project_home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('about/', views.about, name='project_about'),
    
]