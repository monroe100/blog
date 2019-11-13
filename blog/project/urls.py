from django.urls import path
from . import views
from .views import ( 
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,

    BusinessListView,
    BusinessDetailView,
    BusinessCreateView,
    BusinessUpdateView,
    BusinessDeleteView

)

urlpatterns = [
    path('', PostListView.as_view(), name='project_home'),
    path('business', BusinessListView.as_view(), name='business_home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('business/<int:pk>/', BusinessDetailView.as_view(), name='business_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('business/new/', BusinessCreateView.as_view(), name='business_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('business/<int:pk>/update/', BusinessUpdateView.as_view(), name='business_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('business/<int:pk>/delete/', BusinessDeleteView.as_view(), name='business_delete'),
    path('about/', views.about, name='project_about'),
    path('business/', views.about, name='business_about'),
    
]